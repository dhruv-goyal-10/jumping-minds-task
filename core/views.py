from rest_framework import viewsets
from core.models import ElevatorSystem, Elevator, ElevatorRequest
from core.serializers import (
    ElevatorSystemSerializer,
    ElevatorSerializer,
    ElevatorRequestSerializer,
)
from core.renderers import CustomResponseRenderer


class ElevatorSystemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Elevator System to be viewed or edited.
    """

    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer
    renderer_classes = [CustomResponseRenderer]


class ElevatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Elevator to be viewed or edited.
    """

    queryset = Elevator.objects.all().select_related("elevator_system")
    serializer_class = ElevatorSerializer
    renderer_classes = [CustomResponseRenderer]


class ElevatorRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Elevator Request to be viewed or edited.
    """

    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer
    renderer_classes = [CustomResponseRenderer]

    def get_queryset(self):
        elevator_pk = self.kwargs.get("elevator_pk", None)
        if elevator_pk is not None:
            self.queryset = self.queryset.filter(elevator__pk=elevator_pk)
        return self.queryset
