from rest_framework import serializers
from django.contrib.auth.models import User
from weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = '__all__'



