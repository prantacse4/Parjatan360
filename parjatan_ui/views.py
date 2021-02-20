from django.shortcuts import render, HttpResponseRedirect, redirect
from django.db.models import Q
from django.views.generic import CreateView
from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User, UserProfileImage, member, resorts_manager, blogger, car_driver, Tours, tour_arranger
from .forms import UserProfileForm, memberSignUpForm, car_driverSignUpForm, resorts_managerSignUpForm, bloggerSignUpForm, tour_arrangerSignUpForm
# from .decorators import student_required, teacher_required

# Create your views here.


def parjatan_ui(request):
    diction = {}
    return render(request, 'parjatan_ui/index.html', context = diction)


def signup(request):
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
            return redirect('userlogin')
    diction = {'myform':myform}
    
    return render(request, 'parjatan_ui/signup.html', context = diction)



def userlogin(request):
    # if request.user.is_authenticated:
    #     if request.user.is_teacher == True:
    #         return redirect('multiauth_teacher')
    #     elif request.user.is_student == True:
    #         return redirect('multiauth_student')
    #     elif request.user.is_superuser == True:
    #         return  HttpResponseRedirect('/admin')

    if request.method == 'POST':
        logininfo = request.POST.get('username')
        password = request.POST.get('password')
        is_what = False
        is_member =False
        is_tour_arranger = False
        is_resorts_manager = False
        is_car_driver = False
        is_blogger = False
        is_superuser = False
        is_what = User.objects.filter(username=logininfo)
        is_what2 = User.objects.filter(email = logininfo)

        if is_what:
            is_what = User.objects.get(username=logininfo)
            is_member = is_what.is_member
            is_resorts_manager = is_what.is_resorts_manager
            is_tour_arranger = is_what.is_tour_arranger
            is_car_driver = is_what.is_car_driver
            is_blogger = is_what.is_blogger
            is_superuser = is_what.is_superuser

        elif is_what2:
            is_what = User.objects.get(email=logininfo)
            is_member = is_what.is_member
            is_resorts_manager = is_what.is_resorts_manager
            is_tour_arranger = is_what.is_tour_arranger
            is_car_driver = is_what.is_car_driver
            is_blogger = is_what.is_blogger
            is_superuser = is_what.is_superuser

        if is_member == True:
            try:
                user = authenticate(request, username=User.objects.get(email=logininfo), password=password, is_member=True)
            except:
                user = authenticate(request, username=logininfo, password=password, is_member=True)

            if user is not None:
                login(request, user)
                return redirect('parjatan_ui')
            else:
                messages.info(request, 'Wrong username/email or password')
                return redirect('userlogin')
                
        elif is_tour_arranger == True:
            try:
                user = authenticate(request, username=User.objects.get(email=logininfo), password=password, is_tour_arranger=True)
            except:
                user = authenticate(request, username=logininfo, password=password, is_tour_arranger=True)

            if user is not None:
                login(request, user)
                return redirect('parjatan_ui')
            else:
                messages.info(request, 'Wrong username/email or password')
                return redirect('userlogin')


        elif is_resorts_manager == True:
            try:
                user = authenticate(request, username=User.objects.get(email=logininfo), password=password, is_resorts_manager=True)
            except:
                user = authenticate(request, username=logininfo, password=password, is_resorts_manager=True)

            if user is not None:
                login(request, user)
                return redirect('parjatan_ui')
            else:
                messages.info(request, 'Wrong username/email or password')
                return redirect('userlogin')



        elif is_car_driver == True:
            try:
                user = authenticate(request, username=User.objects.get(email=logininfo), password=password, is_car_driver=True)
            except:
                user = authenticate(request, username=logininfo, password=password, is_car_driver=True)

            if user is not None:
                login(request, user)
                return redirect('parjatan_ui')
            else:
                messages.info(request, 'Wrong username/email or password')
                return redirect('userlogin')




        elif is_blogger == True:
            try:
                user = authenticate(request, username=User.objects.get(email=logininfo), password=password, is_blogger=True)
            except:
                user = authenticate(request, username=logininfo, password=password, is_blogger=True)

            if user is not None:
                login(request, user)
                return redirect('parjatan_ui')
            else:
                messages.info(request, 'Wrong username/email or password')
                return redirect('userlogin')



        elif is_superuser==True:
            try:
                user = authenticate(request, username=User.objects.get(email=logininfo), password=password)
            except:
                user = authenticate(request, username=logininfo, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/admin')
            else:
                messages.info(request, 'Wrong username/password')
                return redirect('userlogin')

        else:
            messages.info(request, 'Wrong username/password')
            return redirect('userlogin')

    diction = {}
    return render(request, 'parjatan_ui/login.html', context=diction)



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')



def tour(request,id):
    tour = Tours.objects.get(pk=id)
    diction = {'tour':tour}
    return render(request, 'parjatan_ui/tour.html', context=diction)

