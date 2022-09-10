from django.shortcuts import render
from rest_framework import generics
from geopy.distance import geodesic
from charging_stations.serializers import ChargingStationsListQuerySerializer,ChargingStationsSerializers
from .models import ChargingStation
class GetChargingStations(generics.ListAPIView):
    serializer_class=ChargingStationsSerializers
    def get_queryset(self):
        query = ChargingStationsListQuerySerializer(data=self.request.query_params)
        if(query.is_valid(raise_exception=True)):
            if(bool(query.data.get("city"))):
                print("hsjdfhjlsdjfljsdfldsjlfkds")
                print("this is the cityyyyyy",query.data.get("city"))
                return ChargingStation.objects.filter(city=query.data.get("city"))
            if(bool(query.data.get("latitude"))):
                min_distance_station={
                    "distance":0
                };
                distances=[]
                user_latitude=query.data.get("latitude")
                user_longitude=query.data.get("longitude")
                query_set=ChargingStation.objects.all()
                for station in query_set:
                    station_latitude=station.latitude
                    station_longitude=station.longitude
                    distance=geodesic((user_latitude,user_longitude),(station_latitude,station_longitude)).m
                    distances.append(
                        {
                            "distance":distance,
                            "id":station.id
                        }
                    )
                newlist = sorted(distances, key=lambda d: d['distance'])
                print(newlist[0])
                return ChargingStation.objects.filter(id=newlist[0]["id"])
        return ChargingStation.objects.none()
# Create your views here.
