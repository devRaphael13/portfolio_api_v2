from rest_framework.viewsets import ModelViewSet
from .models import Technology, Experience, Project
from .serializers import TechSerializer, ExpSerializer, ProjSerializer

class TechViewSet(ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechSerializer

class ExpViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExpSerializer
    
class ProjViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjSerializer

