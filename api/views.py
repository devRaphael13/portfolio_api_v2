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

class ProjViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjSerializer
