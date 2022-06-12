from rest_framework.viewsets import ModelViewSet
from event.permissions import (
    CompanyPermissions,
    ContractPermissions,
    EventPermissions,
    CompanyEventsPermissions,
)
from datetime import datetime
from event.models import Company, Contract, Event, CompanyEvents
from event.serializers import (
    CompanySerializer,
    ContractSerializer,
    ContractDetailSerializer,
    EventSerializer,
    EventDetailSerializer,
    CompanyEventsSerializer,
)

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
    permission_classes = [CompanyPermissions]

    def get_queryset(self):
        return Company.objects.all()


class ContractViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContractSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [ContractPermissions]

    def get_queryset(self):
        return Contract.objects.all()

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class EventViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = EventSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [EventPermissions]

    def get_queryset(self):
        return Event.objects.all()


class CompanyEventsViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CompanyEventsSerializer
    permission_classes = [CompanyEventsPermissions]

    def get_queryset(self):
        return CompanyEvents.objects.all()
