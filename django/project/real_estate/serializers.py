from rest_framework import serializers
from .models import Client, Realtor, Apartment, House, Land, Offer, Property

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'

# django/project/real_estate/serializers.py
from rest_framework import serializers
from .models import Apartment, House, Land

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive integer.")
        return value

    def validate(self, data):
        if not data.get('client') or not data.get('realtor') or not data.get('price'):
            raise serializers.ValidationError("Client, realtor, and price are required.")
        property_fields = [data.get("apartment"), data.get("house"), data.get("land")]
        if sum(bool(field) for field in property_fields) != 1:
            raise serializers.ValidationError("Specify only one type of property for the offer.")
        return data

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

from rest_framework import serializers
from .models import Need

class NeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Need
        fields = '__all__'

    def validate(self, data):
        if data['min_price'] > data['max_price']:
            raise serializers.ValidationError("Min price cannot be greater than max price.")
        if data['property_type'] == 'apartment':
            if data.get('min_floor') and data.get('max_floor') and data['min_floor'] > data['max_floor']:
                raise serializers.ValidationError("Min floor cannot be greater than max floor.")
        if data['property_type'] == 'house':
            if data.get('min_floors') and data.get('max_floors') and data['min_floors'] > data['max_floors']:
                raise serializers.ValidationError("Min floors cannot be greater than max floors.")
        return data