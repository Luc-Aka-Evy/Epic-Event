"""epic_event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from authentication.views import UserViewset, UserCreate
from event.views import CompanyViewset, ContractViewset, EventViewset
admin_router = routers.SimpleRouter()
admin_router.register("users", UserViewset, basename="users")

router = routers.SimpleRouter()
router.register("company", CompanyViewset, basename="company")
router.register("contract", ContractViewset, basename="contract")
router.register("event", EventViewset, basename="event")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('epic/auth/', include('rest_framework.urls')),
    path("epic/signup/", UserCreate.as_view(), name="signup"),
    path("epic/", include(admin_router.urls)),
    path("epic/", include(router.urls)),
]
