from django.db import models

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
    commission_share = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from shapely.geometry import Point, Polygon

class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('land', 'Земля'),
    ]
    type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    apartment_number = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.FloatField(
        blank=True, null=True,
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        blank=True, null=True,
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )

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
    apartment = models.ForeignKey(Apartment, on_delete=models.PROTECT, blank=True, null=True)
    house = models.ForeignKey(House, on_delete=models.PROTECT, blank=True, null=True)
    land = models.ForeignKey(Land, on_delete=models.PROTECT, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
