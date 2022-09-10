from django.contrib.auth.models import User,AbstractUser,PermissionsMixin,BaseUserManager,UserManager
from django.db import models

# class CustomUserManager(BaseUserManager):
#     def _create_user(self,  email, password, fullName,**extra_fields):
#         if not email:
#             raise ValueError("Email is not provided")
#         if not password:
#             raise ValueError("Password is not provided")
#         user = self.model(
#             email=self.normalize_email(email),
#             fullName=fullName,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
class Battery(models.Model):
    batter_name=models.CharField(primary_key=True,max_length=255)
    charge_cycles=models.PositiveBigIntegerField(null=True,blank=True)

class Vehicle(models.Model):
    vehicle_type=models.CharField(max_length=255)
    number_plate=models.CharField(max_length=100,unique=True)
    battery_id=models.OneToOneField(to=Battery,on_delete=models.CASCADE)
    user_id=models.OneToOneField(to=User,on_delete=models.CASCADE)

# class User(AbstractUser,PermissionsMixin):
#     email=models.EmailField(db_index=True,unique=True,max_length=254)
#     full_name=models.CharField(max_length=255)
#     objects=UserManager


