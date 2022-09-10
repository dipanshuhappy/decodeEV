import imp
from typing import final
from django.shortcuts import render
# from rest_framework.views import Gener
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from user.models import Vehicle


from user.serializers import LoginSerializer, UserSerializer, VehicleSerializer
class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        loginSerializer=LoginSerializer(data=request.POST)
        if loginSerializer.is_valid(raise_exception=True):
            user=authenticate(request,username=loginSerializer.validated_data["email"].split("@")[0],password=loginSerializer.validated_data["password"])
            # user = User.objects.get(email=loginSerializer.validated_data["email"])
            # authenticate()
            if user is None:
                return Response({"detail":"user not found"}, status=status.HTTP_400_BAD_REQUEST)
            vehicle_id=Vehicle.objects.get(user_id=user.id)
            print(vehicle_id)
            return Response({
                "email":user.get_email_field_name(),
                "first_name":user.first_name,
                "last_name":user.last_name,
                "vehicle_id":vehicle_id.id
            },status=status.HTTP_200_OK)

class GetVehicle(generics.RetrieveAPIView):
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
   

