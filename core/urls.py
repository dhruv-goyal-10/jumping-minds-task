from django.urls import path
from core.views import (
    ElevatorSystemViewSet,
    ElevatorViewSet,
    ElevatorRequestViewSet,
    TimeIncrementViewSet,
)
from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

router = routers.DefaultRouter()
router.register(r"elevator-system", ElevatorSystemViewSet, basename="elevator-system")
router.register(r"elevator", ElevatorViewSet, basename="elevator")
router.register(
    r"elevator-request", ElevatorRequestViewSet, basename="elevator-request"
)

elevator_system_nested_router = NestedSimpleRouter(
    router, r"elevator-system", lookup="elevatorsystem"
)
elevator_system_nested_router.register(
    r"elevator", ElevatorViewSet, basename="elevator"
)
elevator_system_nested_router.register(
    r"request", ElevatorRequestViewSet, basename="request"
)

urlpatterns = [
    path("time-increment", TimeIncrementViewSet.as_view({"post": "post"})),
]

urlpatterns += router.urls + elevator_system_nested_router.urls
