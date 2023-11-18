from rest_framework import viewsets
from core.models import ElevatorSystem, Elevator, ElevatorRequest
from core.serializers import (
    ElevatorSystemSerializer,
    ElevatorSerializer,
    ElevatorRequestSerializer,
)
from core.renderers import CustomResponseRenderer

from core.utils import ElevatorService
from rest_framework.response import Response
from django.db import connection
import json


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
        elevatorsystem_pk = self.kwargs.get("elevatorsystem_pk", None)
        if elevator_pk is not None:
            self.queryset = self.queryset.filter(elevator__pk=elevator_pk)
        if elevatorsystem_pk is not None:
            self.queryset = self.queryset.filter(elevator_system__pk=elevatorsystem_pk)
        return self.queryset


class TimeIncrementViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows Time Increment by 1 Unit
    """

    renderer_classes = [CustomResponseRenderer]

    def post(self, request):
        elevator_systems = ElevatorSystem.objects.all()
        for elevator_system in elevator_systems:
            ElevatorService.service_elevator_system(elevator_system)
        return Response({"message": "Time Incremented by 1 Unit"}, status=200)
