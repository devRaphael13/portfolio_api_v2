from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import Experience, Project, Technology, Service, Profile
from .serializers import ExpSerializer, ProjSerializer, TechSerializer, ServSerializer, ProfileSerializer

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

        if featured and featured == "true":
            queryset = queryset.filter(featured=True)
        return super().filter_queryset(queryset)

class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.first()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ServViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServSerializer

