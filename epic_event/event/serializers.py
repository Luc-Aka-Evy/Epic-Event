from rest_framework import serializers
from django.contrib.auth.models import User
from event.models import Company, Contract, Event, CompanyEvents
from authentication.serializers import UserSerializer


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


class ContractDetailSerializer(serializers.ModelSerializer):

    company = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ["id", "company", "created_time", "updated_time", "signed", "seller"]

    def get_company(self, instance):
        queryset = instance.company
        serializer = CompanySerializer(queryset)
        return serializer.data

    def get_seller(self, instance):
        queryset = instance.seller
        serializer = UserSerializer(queryset)
        return serializer.data


class EventSerializer(serializers.ModelSerializer):

    support = serializers.CharField(write_only=True)

    class Meta:
        model = Event
        fields = ["id", "contract", "description", "date", "adress", "support"]

    def create(self, validated_data):
        event = Event(**validated_data)
        if event.contract.signed == False:
            raise serializers.ValidationError("This contract is not signed yet")
        else:
            company_event = CompanyEvents.objects.create(
                company=event.contract.company.id, event=event.id
            )

            event.save()
            company_event.save()
            return event

    def validate_support(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("There is no user with this username")

        if User.objects.filter(username=value).exists():
            return User.objects.get(username=value)


class EventDetailSerializer(serializers.ModelSerializer):

    contract = serializers.SerializerMethodField()
    support = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "contract", "description", "date", "adress", "support"]

    def get_contract(self, instance):
        queryset = instance.contract
        serializer = ContractSerializer(queryset)
        return serializer.data

    def get_support(self, instance):
        queryset = instance.support
        serializer = UserSerializer(queryset)
        return serializer.data


class CompanyEventsSerializer(serializers.ModelSerializer):

    company = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()

    class Meta:
        model = CompanyEvents
        fields = ["id", "company", "event"]

    def get_company(self, instance):
        queryset = instance.company
        serializer = CompanySerializer(queryset)
        return serializer.data

    def get_event(self, instance):
        queryset = instance.event
        serializer = EventSerializer(queryset)
        return serializer.data
