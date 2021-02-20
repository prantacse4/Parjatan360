from django.contrib import admin
from .models import member
from .models import resorts_manager
from .models import tour_arranger
from .models import car_driver
from .models import User
from .models import UserProfileImage
from .models import blogger
from .models import Tours
# Register your models here.

admin.site.register(User)

@admin.register(member)
class memberAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'user_type', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(resorts_manager)
class resorts_managerAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'user_type', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(tour_arranger)
class tour_arrangerAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'user_type', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(car_driver)
class car_driverAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'user_type', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(blogger)
class bloggerAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'user_type', 'phone', 'district', 'is_active', 'is_verified')

@admin.register(UserProfileImage)
class UserProfileImageAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'image')

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'location', 'budget', 'total_memeber', 'booked_seat', 'age_limit', 'duration_days', 'duration_nights', 'date', 'slider_img1', 'slider_img2', 'slider_img3', 'slider_img4', 'highlight_1', 'highlight_2', 'highlight_3', 'highlight_4', 'highlight_5', 'tour_plan', 'inc_accommodation', 'inc_transportation', 'inc_meals', 'inc_guid', 'inc_additional', 'tour_contact_phone', 'tour_contact_email')