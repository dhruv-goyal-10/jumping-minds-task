# Generated by Django 4.2.7 on 2023-11-17 16:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Elevator",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("available", "Available"),
                            ("busy", "Busy"),
                            ("maintenance", "Maintenance"),
                        ],
                        default="available",
                        max_length=20,
                    ),
                ),
                ("current_floor", models.PositiveIntegerField(default=1)),
                (
                    "destination_floor",
                    models.PositiveIntegerField(blank=True, default=None, null=True),
                ),
                (
                    "door_status",
                    models.CharField(
                        choices=[("open", "Open"), ("close", "Close")],
                        default="open",
                        max_length=10,
                    ),
                ),
            ],
            options={
                "verbose_name": "Elevator",
                "verbose_name_plural": "Elevators",
            },
        ),
        migrations.CreateModel(
            name="ElevatorSystem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("no_of_floors", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name": "Elevator System",
                "verbose_name_plural": "Elevator Systems",
            },
        ),
        migrations.CreateModel(
            name="ElevatorRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("from_floor", models.IntegerField()),
                ("to_floor", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("finished", "Finished"),
                            ("queued", "Queued"),
                            ("processing", "Processing"),
                        ],
                        default="queued",
                        max_length=20,
                    ),
                ),
                (
                    "elevator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="elevator_requests",
                        to="core.elevator",
                    ),
                ),
            ],
            options={
                "verbose_name": "Elevator Request",
                "verbose_name_plural": "Elevator Requests",
            },
        ),
        migrations.AddField(
            model_name="elevator",
            name="elevator_system",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="elevators",
                to="core.elevatorsystem",
            ),
        ),
    ]
