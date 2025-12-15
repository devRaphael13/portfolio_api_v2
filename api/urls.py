from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjViewSet, ExpViewSet, TechViewSet, ServViewSet, ProfileAPIView

router = DefaultRouter()

router.register("api/projects", ProjViewSet)
router.register("api/experiences", ExpViewSet)
router.register("api/technologies", TechViewSet)
router.register("api/services", ServViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/profile/", ProfileAPIView.as_view()),
]