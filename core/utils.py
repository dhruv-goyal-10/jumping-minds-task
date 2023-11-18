from core.models import Elevator, ElevatorRequest
from django.db.models import F, Min, Func


class ElevatorService:
    """
    Service class for elevators.
    """

    @staticmethod
    def service_elevator_system(elevator_system):
        currently_processing_elevator_requests = ElevatorRequest.objects.filter(
            status="processing", elevator_system=elevator_system
        ).select_related("elevator")

        updated_elevators = list()
        updated_elevator_requests = list()
        for elevator_request in currently_processing_elevator_requests:
            elevator = elevator_request.elevator
            elevator.current_floor = elevator.destination_floor
            elevator.destination_floor = None
            elevator.status = "available"
            updated_elevators.append(elevator)

            current_elevator_request = elevator_request
            current_elevator_request.status = "finished"
            updated_elevator_requests.append(current_elevator_request)

        Elevator.objects.bulk_update(
            updated_elevators, ["current_floor", "destination_floor", "status"]
        )
        ElevatorRequest.objects.bulk_update(updated_elevator_requests, ["status"])

        queued_elevator_requests_in_elevator_system = ElevatorRequest.objects.filter(
            status="queued", elevator_system=elevator_system
        ).order_by("id")

        for queued_elevator_request in queued_elevator_requests_in_elevator_system:
            ElevatorService.service_elevator_request(queued_elevator_request)

    @staticmethod
    def service_elevator_request(new_elevator_request):
        elevator_system = new_elevator_request.elevator_system
        from_floor = new_elevator_request.from_floor

        pending_elevator_request = elevator_system.elevator_requests.filter(
            status="queued"
        ).first()

        closest_available_elevator = (
            Elevator.objects.filter(elevator_system=elevator_system, status="available")
            .annotate(
                distance=Min(Func(F("current_floor") - from_floor, function="ABS"))
            )
            .order_by("distance")
            .first()
        )

        if closest_available_elevator:
            if pending_elevator_request:
                currently_serving_elevator_request = pending_elevator_request
            else:
                currently_serving_elevator_request = new_elevator_request

            closest_available_elevator.current_floor = (
                currently_serving_elevator_request.from_floor
            )
            closest_available_elevator.destination_floor = (
                currently_serving_elevator_request.to_floor
            )
            closest_available_elevator.status = "busy"
            closest_available_elevator.door_status = "closed"
            closest_available_elevator.save()

            currently_serving_elevator_request.status = "processing"
            currently_serving_elevator_request.elevator = closest_available_elevator
            currently_serving_elevator_request.save()

        return new_elevator_request
