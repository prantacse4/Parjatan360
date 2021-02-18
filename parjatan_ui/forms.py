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




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileImage
        fields = ['image']

