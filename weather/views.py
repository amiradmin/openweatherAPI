from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from weather.serializers import WeatherSerializer
from classes.openweatherapi import OpenWeather
from weather.models import Weather
from rest_framework import viewsets
from weather.serializers import WeatherSerializer
import datetime
import json


# Create your views here.


class GetWeather(viewsets.ModelViewSet):
    """
    Get response to the OpenWeather webservice and insert selected data to the database.
    """
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    lookup_field = 'city'

    def list(self, request):  # type: GetWeather  # type: Any
        queryset = Weather.objects.all()
        serializer = WeatherSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):  # type: Tuple[Any, ...]  # type: Dict[str, Any]
        print(kwargs['city'])
        city = kwargs['city']
        if city.isalpha():
            jsonData = {}
            weatherObj = OpenWeather()
            result = weatherObj.getWeather(city)
            temperature = result['main']['temp']
            requestTime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

            jsonData['temperature'] = temperature
            jsonData['city'] = city
            jsonData['datetime'] = requestTime

            jsonResult = json.dumps(jsonData)
            jsonResult = json.loads(jsonResult)
            print(type(jsonResult))

            obj = Weather()
            obj.temperature = temperature
            obj.city = city
            obj.datetime = requestTime
            obj.save()
            return Response(jsonResult, status=status.HTTP_200_OK)
        else:
            print("here")
            return Response(status=status.HTTP_400_BAD_REQUEST)
