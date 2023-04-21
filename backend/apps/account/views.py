from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Profiles
from .serializers import ProfileSerializer


class ProfilesView(viewsets.ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializer




