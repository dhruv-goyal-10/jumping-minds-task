from core.models import ElevatorSystem, Elevator, ElevatorRequest
from rest_framework import serializers
from core.utils import ElevatorService


class ElevatorSystemSerializer(serializers.ModelSerializer):
    number_of_elevators = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = ElevatorSystem
        fields = "__all__"

    def validate(self, data):
        super().validate(data)
        number_of_elevators = data.get("number_of_elevators")
        if number_of_elevators < 1:
            raise serializers.ValidationError(
                "Number of elevators must be greater than 0"
            )
        return data

    def create(self, validated_data):
        number_of_elevators = validated_data.pop("number_of_elevators")
        elevator_system = ElevatorSystem.objects.create(**validated_data)

        # Create elevators instances and bulk create them
        elevators = [
            Elevator(elevator_system=elevator_system)
            for _ in range(number_of_elevators)
        ]
        Elevator.objects.bulk_create(elevators)
        return elevator_system


class ElevatorSerializer(serializers.ModelSerializer):
    elevator_system = ElevatorSystemSerializer(read_only=True)

    class Meta:
        model = Elevator
        fields = "__all__"


class ElevatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequest
        fields = "__all__"
        extra_kwargs = {
            "status": {"read_only": True},
            "elevator_system": {"required": True, "allow_null": False},
        }

    def validate(self, data):
        data.pop("elevator", None)
        super().validate(data)
        elevator_system = data.get("elevator_system")
        from_floor = data.get("from_floor")
        to_floor = data.get("to_floor")
        min_floor = min(from_floor, to_floor)
        max_floor = max(from_floor, to_floor)
        if min_floor < 1 or max_floor > elevator_system.no_of_floors:
            raise serializers.ValidationError(
                f"from_floor & to_floor value must be between 0 and {elevator_system.no_of_floors}"
            )
        elif from_floor == to_floor:
            raise serializers.ValidationError("from_floor & to_floor must not be equal")
        return data

    def create(self, validated_data):
        elevator_request = ElevatorRequest.objects.create(**validated_data)
        ElevatorService.service_elevator_request(elevator_request)
        return elevator_request

    def to_representation(self, instance):
        instance = ElevatorRequest.objects.get(pk=instance.pk)
        repr = super().to_representation(instance)
        repr["elevator_system"] = ElevatorSystemSerializer(
            instance.elevator_system
        ).data
        repr["elevator"] = ElevatorSerializer(instance.elevator).data
        return repr
