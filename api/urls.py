from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjViewSet, ExpViewSet, TechViewSet

router = DefaultRouter()

router.register("api/projects", ProjViewSet)
router.register("api/experiences", ExpViewSet)
router.register("api/technologies", TechViewSet)

urlpatterns = [
    path("", include(router.urls))
]