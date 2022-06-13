import django_filters
from .models import Company, Contract, Event, CompanyEvents


class CompanyFilterSet(django_filters.FilterSet):
    """Implements filters to be used with CompanyListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Company
        fields = ["name", "adress", "phone", "email", "type"]


class ContractFilterSet(django_filters.FilterSet):
    """Implements filters to be used with ContractListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Contract
        fields = ["signed", "seller"]


class EventFilterSet(django_filters.FilterSet):
    """Implements filters to be used with EventListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Event
        fields = ["contract", "date", "adress", "support"]


class CompanyEventsFilterSet(django_filters.FilterSet):
    """Implements filters to be used with EventListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = CompanyEvents
        fields = ["company"]
