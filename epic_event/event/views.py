from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import AllowAny
from event.models import Company, Contract, Event, Location
from event.serializers import CompanySerializer, ContractSerializer, EventSerializer, LocationSerializer
# Create your views here.



class MultipleSerializerMixin:
    # Un mixin est une classe qui ne fonctionne pas de façon autonome
    # Elle permet d'ajouter des fonctionnalités aux classes qui les étendent

    detail_serializer_class = None

    def get_serializer_class(self):
        # Notre mixin détermine quel serializer à utiliser
        # même si elle ne sait pas ce que c'est ni comment l'utiliser
        if self.action == "retrieve" and self.detail_serializer_class is not None:
            # Si l'action demandée est le détail alors nous retournons le serializer de détail
            return self.detail_serializer_class
        return super().get_serializer_class()


class CompanyViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CompanySerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace']
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        return Company.objects.all()


class ContractViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContractSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Contract.objects.all()


class EventViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = EventSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Event.objects.all()


class LocationViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = LocationSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Location.objects.all()