from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import LiveVideo
from .serializers import LiveVideoSerializer

class LiveVideoViewSet(viewsets.ModelViewSet):
    queryset = LiveVideo.objects.all()
    serializer_class = LiveVideoSerializer
    # Implement other necessary view methods
