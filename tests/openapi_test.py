from django.urls import reverse
from rest_framework import status
import sys
import pytest
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient
from classes.openweatherapi import OpenWeather


def test_get_city_for_check_status_code_equals_200():
    """
    Testing connection to OpenWather webservice.
    """
    city = 'tehran'
    obj = OpenWeather()
    response = obj.getWeather(city)  # type: str
    assert response['cod'] == status.HTTP_200_OK
