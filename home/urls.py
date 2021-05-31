from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('services',views.services,name='services'),
    path('contact',views.form,name='form'),
]

