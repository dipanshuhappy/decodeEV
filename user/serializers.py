from rest_framework import serializers
from django.contrib.auth.models import User

from user.models import Vehicle


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)
    def create(self, validated_data):
        username=validated_data["email"].split("@")[0]
        return User.objects.create_user(username=username,**validated_data)
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=2)
    class Meta:
        model = User
        fields = ['email', 'password']
class VehicleSerializer(serializers.ModelSerializer):
     class Meta:
        model=Vehicle
        fields=[
            'id',
            'bennett_email',
            'first_name',
            'last_name',
            'enrollment_number',
            'school_code',
            'department_code',
            'batch',
            'program',
            'current_semester'
        ]