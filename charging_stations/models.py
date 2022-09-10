from django.db import models

from user.models import Battery, Vehicle

class ChargingStation(models.Model):
    location = models.CharField(max_length=255,default="")
    latitude = models.DecimalField(decimal_places=6,max_digits=8,default=0)
    longitude = models.DecimalField(decimal_places=6,max_digits=8,default=0)
    city = models.CharField(max_length=200,default="")
    number_of_slots = models.PositiveIntegerField(default=0)

class ChargingSlot(models.Model):
    battery_name=models.OneToOneField(to=Battery,on_delete=models.CASCADE)
    is_active  = models.BooleanField()
    charge_percentage = models.DecimalField(decimal_places=2,max_digits=5);
    vehicle_alloted = models.OneToOneField(to=Vehicle,on_delete=models.CASCADE)
    charging_station = models.OneToOneField(to=ChargingStation,on_delete=models.CASCADE)
    otp = models.IntegerField()
