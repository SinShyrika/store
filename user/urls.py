from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from user import views
from user.views import (EmailVerificationView, UserLoginView, UserProfileView,
                        UserRegistrationView)

app_name = 'users'

urlpatterns = [
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('registration/',views.UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>',login_required(views.UserProfileView.as_view()), name='profile'),
    path('logout/',views.logout, name='logout'),
    path('verify/<str:email>/<uuid:code>', EmailVerificationView.as_view(), name='verify'),

]