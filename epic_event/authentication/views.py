from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import AllowAny
from authentication.models import User
from authentication.serializers import UserSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
# Create your views here.
