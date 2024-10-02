from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Experience, Project, Technology
from .serializers import ExpSerializer, ProjSerializer, TechSerializer

class TechViewSet(ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechSerializer

class ExpViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExpSerializer

    def filter_queryset(self, queryset):
        params = self.request.query_params
        featured = params.get("featured")

        if featured:
            queryset = queryset.filter(featured=True)
        return super().filter_queryset(queryset)

class ProjViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjSerializer

    def filter_queryset(self, queryset):
        params = self.request.query_params
        featured = params.get("featured")

        if featured == "true":
            queryset = queryset.filter(featured=True)

        else:
            queryset = queryset.filter(featured=False)
        return super().filter_queryset(queryset)
