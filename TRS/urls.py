"""TRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from user import views as user_views
from booking import views as booking_views


urlpatterns = [
    url('^apiv1/login/', user_views.UserLogin.as_view()),
    url('^apiv1/register/', user_views.UserRegister.as_view()),
    url('^apiv1/login-final/', user_views.UserLoginFinal.as_view()),
    url('^apiv1/make-booking/', booking_views.CreateBooking.as_view()),
    url('^apiv1/list-booking/', booking_views.ListBooking.as_view()),

]
