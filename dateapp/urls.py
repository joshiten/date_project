
from django.contrib import admin
from django.urls import path,include
from dateapp import views

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('yes/',views.YesView,name='yes'),
]
