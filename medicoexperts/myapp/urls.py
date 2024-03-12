"""
URL configuration for medicoexperts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('doctor-profile', views.doctor_profile, name='doctor-profile'),
    path('doctor-profile-update', views.doctor_profile_update, name='doctor-profile-update'),
    path('doctors', views.doctors, name='doctors'),
    path('change-password', views.change_password, name='change-password'),
    # path('doctor-home', views.doctor_home, name='doctor-home'),
    path('logout', views.logout, name='logout'),
]