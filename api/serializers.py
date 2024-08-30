from itertools import chain
from rest_framework.serializers import ModelSerializer
from .models import Technology, Experience, Project

class TechRepr:

    def to_representation(self, instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.name for i in f.value_from_object(instance)]
        return data

class TechSerializer(ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"

class ExpSerializer(TechRepr, ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"

class ProjSerializer(TechRepr, ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"