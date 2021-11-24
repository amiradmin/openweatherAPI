from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from weather.models import Weather
import json

class WeatherTests(APITestCase):
    def test_get_city_temp(self):
        """
        Ensure we get response and seve it in database.
        """
        city ='tehran'
        url = reverse('weather-detail',args=[city])
        print(url)
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response_data)
        self.assertEqual(Weather.objects.count(), 1)
        self.assertEqual(Weather.objects.get().city, city)


