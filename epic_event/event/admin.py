from django.contrib import admin
from event.models import Company, Contract, Event

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "adress", "phone", "email", "type")


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("company", "created_time", "updated_time", "signed", "seller")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("contract", "description", "adress", "date", "created_time", "updated_time", "support")
