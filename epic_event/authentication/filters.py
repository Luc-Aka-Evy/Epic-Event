import django_filters
from .models import User, Profile


class UserFilterSet(django_filters.FilterSet):
    """Implements filters to be used with CompanyListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class ProfileFilterSet(django_filters.FilterSet):
    """Implements filters to be used with CompanyListView."""

    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Profile
        fields = ["user", "birth_date", "phone_number", "gender"]
