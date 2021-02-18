from django.shortcuts import render, HttpResponseRedirect, redirect
from django.db.models import Q
from django.views.generic import CreateView
from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User, UserProfileImage, member, resorts_manager, blogger, car_driver
from .forms import UserProfileForm, memberSignUpForm, car_driverSignUpForm, resorts_managerSignUpForm, bloggerSignUpForm, tour_arrangerSignUpForm
# from .decorators import student_required, teacher_required

# Create your views here.


def parjatan_ui(request):
    diction = {}
    return render(request, 'parjatan_ui/index.html', context = diction)

def login(request):
    diction = {}
    return render(request, 'parjatan_ui/login.html', context = diction)


def signup(request):
    # if request.user.is_authenticated:
    #     if request.user.is_teacher == True:
    #         return redirect('multiauth_teacher')
    #     elif request.user.is_student == True:
    #         return redirect('multiauth_student')
    #     elif request.user.is_superuser == True:
    #         return  HttpResponseRedirect('/admin')

    myform = memberSignUpForm()
    if request.method == 'POST':
        myform = memberSignUpForm(request.POST)
        

        if myform.is_valid():
            user_type = myform.cleaned_data['user_type']
            if user_type == 'member':
                myform =myform
            elif user_type == 'tour_arranger':
                myform = tour_arrangerSignUpForm(request.POST)
            elif user_type == 'car_driver':
                myform = car_driverSignUpForm(request.POST)
            elif user_type == 'resort_manager':
                myform = resorts_managerSignUpForm(request.POST)
            elif user_type == 'blogger':
                myform = bloggerSignUpForm(request.POST)
            myform.save()
            user = myform.cleaned_data.get('username')
            messages.success(request, 'Account Created for '+ user)
            return redirect('login')
    diction = {'myform':myform}
    
    return render(request, 'parjatan_ui/signup.html', context = diction)