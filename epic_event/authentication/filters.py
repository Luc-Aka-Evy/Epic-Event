import django_filters
from .models import User, Profile


class UserFilterSet(django_filters.FilterSet):
    """Implements filters to be used with CompanyListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")
    sort_by = django_filters.CharFilter(
        method="filter_sort_by",
        label="Sort by a given value (username, email, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(",")
        return queryset.order_by(*values)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "sort_by"]


class ProfileFilterSet(django_filters.FilterSet):
    """Implements filters to be used with CompanyListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")
    sort_by = django_filters.CharFilter(
        method="filter_sort_by",
        label="Sort by a given value (user,gender, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(",")
        return queryset.order_by(*values)

    class Meta:
        model = Profile
        fields = ["user", "birth_date", "phone_number", "gender", "sort_by"]
