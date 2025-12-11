from itertools import chain
from rest_framework.serializers import ModelSerializer
from .models import Technology, Experience, Project

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
