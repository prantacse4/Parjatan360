from django.contrib import admin
from .models import member
from .models import resorts_manager
from .models import tour_arranger
from .models import car_driver
from .models import User
from .models import UserProfileImage
from .models import blogger
# Register your models here.

admin.site.register(User)

@admin.register(member)
class memberAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'email', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(resorts_manager)
class resorts_managerAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'email', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(tour_arranger)
class tour_arrangerAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'email', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(car_driver)
class car_driverAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'email', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(blogger)
class bloggerAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'email', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(UserProfileImage)
class UserProfileImageAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'image')