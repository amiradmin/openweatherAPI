from django.urls import include, path
from rest_framework import routers
from weather import views


app_name ="weather"
urlpatterns = [

    path('weather', views.GetWeather.as_view(), name='weather_'),




]
