from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_member  = models.BooleanField(default=False)
    is_tour_arranger  = models.BooleanField(default=False)
    is_resorts_manager  = models.BooleanField(default=False)
    is_car_driver  = models.BooleanField(default=False)
    is_blogger  = models.BooleanField(default=False)

class member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    is_active = models.BooleanField(default = False)
    is_verified = models.BooleanField(default=False)



class tour_arranger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    is_active = models.BooleanField(default = False)
    is_verified = models.BooleanField(default=False)


class resorts_manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    is_active = models.BooleanField(default = False)
    is_verified = models.BooleanField(default=False)

class car_driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    is_active = models.BooleanField(default = False)
    is_verified = models.BooleanField(default=False)

class blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    is_active = models.BooleanField(default = False)
    is_verified = models.BooleanField(default=False)


class UserProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to="uploaded_image/user")