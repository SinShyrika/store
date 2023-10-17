from django.contrib import admin
from django.urls import path
from user import views
app_name = 'users'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('registration/',views.registration, name='registration'),
]