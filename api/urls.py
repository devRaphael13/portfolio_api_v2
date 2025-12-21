from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MsgViewSet, ProjViewSet, ExpViewSet, TechViewSet, ServViewSet, ProfileViewSet

router = DefaultRouter()

router.register("api/projects", ProjViewSet)
router.register("api/experiences", ExpViewSet)
router.register("api/technologies", TechViewSet)
router.register("api/services", ServViewSet)
router.register("api/profile", ProfileViewSet, basename="profile")
router.register("api/messages", MsgViewSet)

urlpatterns = [
    path("", include(router.urls))
]