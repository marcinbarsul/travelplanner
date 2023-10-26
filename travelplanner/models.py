from django.db import models

class Trip(models.Model):
    country = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    cities_visited = models.TextField(default="Trip direction")

class Hotel(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()

class Flight(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    airline = models.CharField(max_length=20)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    visa = models.BooleanField(default=False)
    visa_price = models.IntegerField(null=True, blank=True, help_text='(U.S. Dollar)')
    visa_duration = models.IntegerField(null=True, blank=True, help_text='(in days)')


class Attraction(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    countries = models.CharField(max_length=20, blank=True, null=True)

class Basket(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    flight_costs = models.DecimalField(max_digits=10, decimal_places=2, help_text='(U.S. Dollar)')
    hotel_costs = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,  help_text='(U.S. Dollar)')
    attraction_costs = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,  help_text='(U.S. Dollar)')
