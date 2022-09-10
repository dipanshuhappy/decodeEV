from django.contrib import admin

from charging_stations.models import ChargingSlot, ChargingStation

admin.site.register(ChargingStation)
admin.site.register(ChargingSlot)
# Register your models here.
