from django.contrib import admin
from .models import Client, Realtor

admin.site.register(Client)
admin.site.register(Realtor)

from django.contrib import admin
from .models import Apartment, House, Land, Offer

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'house_number', 'apartment_number', 'floor', 'rooms', 'area']
    search_fields = ['city', 'street', 'house_number', 'apartment_number']

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'house_number', 'floors', 'rooms', 'area']
    search_fields = ['city', 'street', 'house_number']

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'house_number', 'area']
    search_fields = ['city', 'street', 'house_number']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['description', 'price', 'apartment', 'house', 'land']
    search_fields = ['description']

