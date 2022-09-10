from dataclasses import fields
from rest_framework import serializers
from .models import ChargingStation
class ChargingStationsListQuerySerializer(serializers.Serializer):
    city=serializers.CharField(max_length=200,default="",required=False)
    latitude=serializers.DecimalField(default=0,decimal_places=6,max_digits=8,required=False)
    longitude = serializers.DecimalField(decimal_places=6,max_digits=8,default=0,required=False)
    def validate(self, data):
        if not(bool(data.get("city")) or bool(data.get("latitude"))):
            raise serializers.ValidationError("Need at least city or latitude")
        return data
class ChargingStationsSerializers(serializers.ModelSerializer):
    class Meta:
        model=ChargingStation
        fields=[
           
            'location',
            'latitude',
            'longitude',
            'city',
            'number_of_slots'
        ]