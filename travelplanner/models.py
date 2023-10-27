from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
class Trip(models.Model):
    country = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    cities_visited = models.TextField(default="Trip direction")

    def __str__(self):
        return self.country

class Hotel(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Flight(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    airline = models.CharField(max_length=20)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    visa = models.BooleanField(default=False)
    visa_price = models.IntegerField(null=True, blank=True, help_text='(U.S. Dollar)')
    visa_duration = models.IntegerField(null=True, blank=True, help_text='(in days)')

    def __str__(self):
        return self.airline


class Attraction(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    countries = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Basket(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    flight_costs = models.DecimalField(max_digits=10, decimal_places=2, help_text='(U.S. Dollar)')
    hotel_costs = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,  help_text='(U.S. Dollar)')
    attraction_costs = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,  help_text='(U.S. Dollar)')
    total_costs = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text='(U.S. Dollar)')
@receiver(pre_save, sender=Basket)
def update_total_costs(sender, instance, **kwargs):
    instance.total_costs = instance.flight_costs + instance.hotel_costs + instance.attraction_costs