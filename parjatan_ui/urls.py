from django.contrib import admin
from django.urls import path
from parjatan_ui import views

urlpatterns = [
    path('',views.parjatan_ui, name="parjatan_ui"),
]