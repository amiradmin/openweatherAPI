from django.urls import reverse
from rest_framework import status
import sys
import pytest
sys.path.append("/home/amir/challageWeather/mysite")
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient


def test_get_locations_for_us_90210_check_status_code_equals_200():

    client = RequestsClient()
    response = client.get('http://api.openweathermap.org/data/2.5/weather?q=tehran&units=metric&appid=d0e239f15d5f56006808fd1cf63f968c')
    assert response.status_code == 200