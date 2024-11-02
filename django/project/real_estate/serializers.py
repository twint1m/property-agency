from rest_framework import serializers
from .models import Client, Realtor

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'

from rest_framework import serializers
from .models import Apartment, House, Land, Offer

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class ApartmentSerializer(PropertySerializer):
    class Meta(PropertySerializer.Meta):
        model = Apartment

class HouseSerializer(PropertySerializer):
    class Meta(PropertySerializer.Meta):
        model = House

class LandSerializer(PropertySerializer):
    class Meta(PropertySerializer.Meta):
        model = Land

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def validate(self, data):
        property_fields = [data.get("apartment"), data.get("house"), data.get("land")]
        if sum(bool(field) for field in property_fields) != 1:
            raise serializers.ValidationError("Укажите только один тип недвижимости для предложения.")
        return data
