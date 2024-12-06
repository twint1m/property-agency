from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

class Realtor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    commission_share = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Property(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    apartment_number = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        abstract = True

class Apartment(Property):
    floor = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

class House(Property):
    floors = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

class Land(Property):
    area = models.FloatField(blank=True, null=True)

class Offer(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='offers', blank=True, null=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.PROTECT, related_name='offers', blank=True, null=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.PROTECT, blank=True, null=True)
    house = models.ForeignKey(House, on_delete=models.PROTECT, blank=True, null=True)
    land = models.ForeignKey(Land, on_delete=models.PROTECT, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models

class Need(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('land', 'Land'),
    ]

    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    realtor = models.ForeignKey(Realtor, on_delete=models.PROTECT)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES)
    address = models.CharField(max_length=255)
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    min_area = models.PositiveIntegerField(null=True, blank=True)
    max_area = models.PositiveIntegerField(null=True, blank=True)
    min_rooms = models.PositiveIntegerField(null=True, blank=True)
    max_rooms = models.PositiveIntegerField(null=True, blank=True)
    min_floor = models.PositiveIntegerField(null=True, blank=True)
    max_floor = models.PositiveIntegerField(null=True, blank=True)
    min_floors = models.PositiveIntegerField(null=True, blank=True)
    max_floors = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.client} - {self.property_type} need"