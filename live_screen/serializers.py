from rest_framework import serializers
from .models import LiveVideo

class LiveVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveVideo
        fields = '__all__'
