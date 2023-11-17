from core.models import ElevatorSystem, Elevator, ElevatorRequest
from django.db.models import F, Min, Func


class ElevatorService:
    """
    Service class for elevators.
    """

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
