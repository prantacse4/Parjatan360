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


class Tours(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    budget = models.IntegerField()
    total_memeber = models.IntegerField()
    booked_seat = models.IntegerField()
    age_limit = models.CharField(max_length=50)
    duration_days = models.IntegerField()
    duration_nights = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    slider_img1 = models.ImageField(upload_to="uploaded_image/slider")
    slider_img2 = models.ImageField(upload_to="uploaded_image/slider")
    slider_img3 = models.ImageField(upload_to="uploaded_image/slider")
    slider_img4 = models.ImageField(upload_to="uploaded_image/slider")
    highlight_1 = models.CharField(max_length=150)
    highlight_2 = models.CharField(max_length=150)
    highlight_3 = models.CharField(max_length=150)
    highlight_4 = models.CharField(max_length=150)
    highlight_5 = models.CharField(max_length=150)
    tour_plan = models.TextField()
    promo_text = models.TextField()
    inc_accommodation = models.TextField()
    inc_transportation = models.TextField()
    inc_meals = models.TextField()
    inc_guid = models.TextField()
    inc_additional = models.TextField()
    tour_contact_phone = models.CharField(max_length=150)
    tour_contact_email = models.CharField(max_length=150)
