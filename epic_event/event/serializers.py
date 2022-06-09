from rest_framework import serializers
from event.models import Company, Contract, Event


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "adress", "phone", "email", "type"]

    
    def validate_name(self, value):
        if Company.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "There is already a company with this name"
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

    company = serializers.CharField(write_only=True)

    class Meta:
        model = Contract
        fields = ["id", "company", "signed"]


    def validate_company(self, value):
        if not Company.objects.filter(name=value).exists():
            raise serializers.ValidationError("There is no company with this name")

        if Company.objects.filter(name=value).exists():
            return Company.objects.get(name=value)


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ["id", "contract", "description", "start", "end", "adress", "support"]
