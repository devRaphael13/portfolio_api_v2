from tkinter import N
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

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

class ProfileViewSet(ViewSet):
    profile = Profile.objects.first()

    def list(self, request, *args, **kwargs):
        serializer = ProfileSerializer(self.profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False)
    def resume(self, request, *args, **kwargs):
        resume_url = None

        if self.profile.resume:
            resume_url = self.profile.resume.url

        data = {
            "resume": resume_url
        }

        return Response(data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False)
    def profile_img(self, request, *args, **kwargs):
        image_url = None

        if self.profile.profile_img:
            image_url = self.profile.profile_img.url

        data = {
            "profile_img": image_url
        }

        return Response(data, status=status.HTTP_200_OK)


class ServViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServSerializer

