from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django_filters import rest_framework as filters
from event.permissions import IsAdmin
from authentication.models import User, Profile
from authentication.serializers import UserSerializer, ProfileSerializer
from .filters import UserFilterSet, ProfileFilterSet


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UserFilterSet
    http_method_names = ["get", "post", "patch", "delete", "head", "options", "trace"]

    def get_queryset(self):
        return User.objects.all()


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class ProfileViewset(ModelViewSet):

    serializer_class = ProfileSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProfileFilterSet
    http_method_names = ["get", "post", "patch", "delete", "head", "options", "trace"]

    def get_queryset(self):
        return Profile.objects.all()


# Create your views here.
