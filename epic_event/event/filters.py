import django_filters
from .models import Company, Contract, Event


class CompanyFilterSet(django_filters.FilterSet):
    """Implements filters to be used with CompanyListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")
    sort_by = django_filters.CharFilter(
        method="filter_sort_by",
        label="Sort by a given value (name,company, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(",")
        return queryset.order_by(*values)

    class Meta:
        model = Company
        fields = ["name", "adress", "phone", "email", "type", "sort_by"]


class ContractFilterSet(django_filters.FilterSet):
    """Implements filters to be used with ContractListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")
    sort_by = django_filters.CharFilter(
        method="filter_sort_by",
        label="Sort by a given value (signed,company, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(",")
        return queryset.order_by(*values)

    class Meta:
        model = Contract
        fields = ["company", "signed", "seller", "sort_by"]


class EventFilterSet(django_filters.FilterSet):
    """Implements filters to be used with EventListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")
    sort_by = django_filters.CharFilter(
        method="filter_sort_by",
        label="Sort by a given value (description,company, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(",")
        return queryset.order_by(*values)

    class Meta:
        model = Event
        fields = ["company", "contract", "date", "adress", "support"]
