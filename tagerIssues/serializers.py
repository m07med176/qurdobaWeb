from .models import CodesOfServices
from rest_framework import serializers

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodesOfServices
        fields = '__all__'