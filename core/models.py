from django.db import models
import uuid


class ElevatorSystem(models.Model):

    """
    Model to represent an elevator system.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    no_of_floors = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Elevator System"
        verbose_name_plural = "Elevator Systems"


class Elevator(models.Model):

    """
    Model to represent an elevator.
    """

    ELEVATOR_STATUS_CHOICES = (
        ("available", "Available"),
        ("busy", "Busy"),
        ("maintenance", "Maintenance"),
    )

    ELEVATOR_DOOR_CHOICES = (
        ("open", "Open"),
        ("close", "Close"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    elevator_system = models.ForeignKey(
        ElevatorSystem, related_name="elevators", on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20, choices=ELEVATOR_STATUS_CHOICES, default="available"
    )
    current_floor = models.PositiveIntegerField(default=1)
    destination_floor = models.PositiveIntegerField(default=None, blank=True, null=True)
    door_status = models.CharField(
        max_length=10, choices=ELEVATOR_DOOR_CHOICES, default="open"
    )

    def __str__(self) -> str:
        return f"{self.elevator_system.name} {self.id} ({self.status})"

    class Meta:
        verbose_name = "Elevator"
        verbose_name_plural = "Elevators"


class ElevatorRequest(models.Model):

    """
    Model to represent a request for an elevator.
    """

    REQUEST_STATUS = (
        ("finished", "Finished"),
        ("queued", "Queued"),
        ("processing", "Processing"),
    )

    elevator = models.ForeignKey(
        Elevator,
        related_name="elevator_requests",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    from_floor = models.IntegerField()
    to_floor = models.IntegerField()
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, default="queued")

    def __str__(self) -> str:
        return f"{self.id} ({self.status})"

    class Meta:
        verbose_name = "Elevator Request"
        verbose_name_plural = "Elevator Requests"
