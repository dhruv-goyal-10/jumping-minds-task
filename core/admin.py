from django.contrib import admin
from core.models import ElevatorSystem, Elevator, ElevatorRequest


class ElevatorSystemAdmin(admin.ModelAdmin):
    list_display = ("name", "no_of_floors")


class ElevatorAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "current_floor",
        "destination_floor",
        "door_status",
    )


class ElevatorRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "from_floor",
        "to_floor",
        "status",
    )


admin.site.register(ElevatorSystem, ElevatorSystemAdmin)
admin.site.register(Elevator, ElevatorAdmin)
admin.site.register(ElevatorRequest, ElevatorRequestAdmin)
