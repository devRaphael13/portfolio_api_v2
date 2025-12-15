from itertools import chain
from rest_framework.serializers import ModelSerializer
from .models import Technology, Experience, Project, Service, Profile

class TechSerializer(ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"

class ExpSerializer(ModelSerializer):
    tech_used = TechSerializer(many=True)
    class Meta:
        model = Experience
        fields = "__all__"

class ProjSerializer(ModelSerializer):
    tech_used = TechSerializer(many=True)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Ensure thumbnail returns URL string
        if instance.thumbnail:
            representation['thumbnail'] = str(instance.thumbnail.url)
        return representation
    
    class Meta:
        model = Project
        fields = "__all__"

class ServSerializer(ModelSerializer):
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Ensure thumbnail returns URL string
        if instance.thumbnail:
            representation['thumbnail'] = str(instance.thumbnail.url)
        return representation

    class Meta:
        model = Service
        fields = "__all__"

class ProfileSerializer(ModelSerializer):
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.profile_img:
            representation['profile_img'] = str(instance.profile_img.url)
        if instance.resume:
            representation['resume'] = str(instance.resume.url)
        return representation

    class Meta:
        model = Profile
        fields = "__all__"

