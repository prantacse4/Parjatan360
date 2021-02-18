from django.core import validators
from django import forms
from .models import User, UserProfileImage, blogger, car_driver, resorts_manager, tour_arranger, member
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User






class memberSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    user_type = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    district = forms.CharField(required=True)
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_member = True
        user.save()
        memberDetails = member.objects.create(user=user)
        memberDetails.name = self.cleaned_data.get('name')
        memberDetails.user_type = self.cleaned_data.get('user_type')
        memberDetails.phone = self.cleaned_data.get('phone')
        memberDetails.district = self.cleaned_data.get('district')
        memberDetails.save()
        return memberDetails



class car_driverSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    user_type = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    district = forms.CharField(required=True)
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_member = True
        user.save()
        car_driverDetails = car_driver.objects.create(user=user)
        car_driverDetails.name = self.cleaned_data.get('name')
        car_driverDetails.user_type = self.cleaned_data.get('user_type')
        car_driverDetails.phone = self.cleaned_data.get('phone')
        car_driverDetails.district = self.cleaned_data.get('district')
        car_driverDetails.save()
        return car_driverDetails



class resorts_managerSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    user_type = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    district = forms.CharField(required=True)
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_member = True
        user.save()
        resorts_managerDetails = resorts_manager.objects.create(user=user)
        resorts_managerDetails.name = self.cleaned_data.get('name')
        resorts_managerDetails.user_type = self.cleaned_data.get('user_type')
        resorts_managerDetails.phone = self.cleaned_data.get('phone')
        resorts_managerDetails.district = self.cleaned_data.get('district')
        resorts_managerDetails.save()
        return resorts_managerDetails




class bloggerSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    user_type = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    district = forms.CharField(required=True)
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_member = True
        user.save()
        bloggerDetails = blogger.objects.create(user=user)
        bloggerDetails.name = self.cleaned_data.get('name')
        bloggerDetails.user_type = self.cleaned_data.get('user_type')
        bloggerDetails.phone = self.cleaned_data.get('phone')
        bloggerDetails.district = self.cleaned_data.get('district')
        bloggerDetails.save()
        return bloggerDetails



class tour_arrangerSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    user_type = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    district = forms.CharField(required=True)
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_member = True
        user.save()
        tour_arrangerDetails = tour_arranger.objects.create(user=user)
        tour_arrangerDetails.name = self.cleaned_data.get('name')
        tour_arrangerDetails.user_type = self.cleaned_data.get('user_type')
        tour_arrangerDetails.phone = self.cleaned_data.get('phone')
        tour_arrangerDetails.district = self.cleaned_data.get('district')
        tour_arrangerDetails.save()
        return tour_arrangerDetails




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileImage
        fields = ['image']

