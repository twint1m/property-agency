from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Realtor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Property(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    area = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        abstract = True

class Apartment(Property):
    floor = models.IntegerField(validators=[MinValueValidator(0)])
    rooms = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Apartment: {self.city}, {self.street}, {self.house_number}, {self.apartment_number}"

class House(Property):
    floors = models.IntegerField(validators=[MinValueValidator(1)])
    rooms = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"House: {self.city}, {self.street}, {self.house_number}"

class Land(Property):
    def __str__(self):
        return f"Land: {self.city}, {self.street}, {self.house_number}"

class Offer(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, blank=True, null=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, blank=True, null=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Offer: {self.client} - {self.price}"

class Need(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=20, choices=[('apartment', 'Apartment'), ('house', 'House'), ('land', 'Land')])
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    min_area = models.FloatField(validators=[MinValueValidator(0.0)])
    max_area = models.FloatField(validators=[MinValueValidator(0.0)])
    min_floor = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    max_floor = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    min_floors = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    max_floors = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)

    def __str__(self):
        return f"Need: {self.client} - {self.property_type}"

class Deal(models.Model):
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Deal: {self.need} - {self.offer}"

class Event(models.Model):
    EVENT_TYPES = [
        ('meeting', 'Meeting with Client'),
        ('showing', 'Showing'),
        ('call', 'Scheduled Call')
    ]

    datetime = models.DateTimeField()
    duration = models.DurationField(blank=True, null=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Event: {self.event_type} on {self.datetime}"