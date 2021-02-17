from django.shortcuts import render, HttpResponseRedirect, redirect
from django.db.models import Q
from django.views.generic import CreateView
from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# from .models import User, Teacher, Student, UserProfileImage
# from .forms import StudentSignUpForm, TeacherSignUpForm, UserProfileForm, StudentUpdateForm, TeacherUpdateForm
# from .decorators import student_required, teacher_required

# Create your views here.


def parjatan_ui(request):
    diction = {}
    return render(request, 'parjatan_ui/index.html', context = diction)

def login(request):
    diction = {}
    return render(request, 'parjatan_ui/login.html', context = diction)

def signup(request):
    diction = {}
    return render(request, 'parjatan_ui/signup.html', context = diction)