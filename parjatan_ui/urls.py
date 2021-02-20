from django.contrib import admin
from django.urls import path
from parjatan_ui import views

urlpatterns = [
    path('',views.parjatan_ui, name="parjatan_ui"),
    path('login/',views.userlogin, name="userlogin"),
    path('signup/',views.signup, name="signup"),
    path('logout/',views.logout_user, name="logout_user"),
    path('tour/<int:id>/', views.tour, name="tour"),


]