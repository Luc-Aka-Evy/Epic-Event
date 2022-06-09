from rest_framework import serializers
from event.models import Company, Contract, Event, Location


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "adress", "phone", "email", "type"]

    
    def validate_name(self, value):
        if Company.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "There is alreadyy a company with this name"
            )
        return value

    def validate_email(self, value):
        if Company.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already use by another company"
            )
        return value

    def validate_phone(self, value):
        if Company.objects.filter(phone=value).exists():
            raise serializers.ValidationError(
                "This number is already use by another company"
            )
        return value

    
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "company", "signed", "seller"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "contract", "description", "start", "end", "location", "support"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "adress", "postcode"]