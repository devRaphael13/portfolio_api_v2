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

    class Meta:
        model = Project
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.thumbnail:
            representation['thumbnail'] = str(instance.thumbnail.url)
        return representation

class ServSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

    def update(self, instance, validated_data):
        features = validated_data.get("features")
        merged = instance.features + features
        validated_data['features'] = list(dict.fromkeys(merged))
        return super().update(instance, validated_data)
class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.profile_img:
            representation['profile_img'] = str(instance.profile_img.url)
        if instance.resume:
            representation['resume'] = str(instance.resume.url)
        return representation
