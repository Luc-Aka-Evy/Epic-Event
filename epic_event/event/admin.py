from django.contrib import admin
from event.models import Company, CompanyEvents, Contract, Event

# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyEvents)
admin.site.register(Contract)
admin.site.register(Event)
