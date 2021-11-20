from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from weather.serializers import WeatherSerializer
from classes.openweatherapi import OpenWeather
from weather.models import Weather
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from weather.serializers import UserSerializer, GroupSerializer
# Create your views here.

# class GetWeather(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     # queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         print("OK")
#         return []
#
#     def list(self, request):
#         print("List")
#         queryset = Weather.objects.all()
#         serializer = WeatherSerializer(queryset, many=True)
#         return Response(serializer.data)


class GetWeather(viewsets.ViewSet):

    def get_queryset(self):
        print("OK")
        return []

    def list(self, request):
        print("List")
        queryset = Weather.objects.all()
        serializer = WeatherSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None,*args,**kwargs):
        # print(kwargs['id'])
        print(pk)
        queryset = Weather.objects.filter(pk=pk)
        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = WeatherSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# class GetWeather(APIView):
#
#     @classmethod
#     def get_extra_actions(cls):
#         print("Extra")
#         return []


    # def get(self, request, format=None):
    #     print("Here")
    #     city = self.request.query_params.get('city', None)
    #     if city is not None:
    #         obj = OpenWeather()
    #         print(obj.getWeather(city))
    #     result = {
    #         "status": False,
    #         "msg": "Done"
    #     }
    #
    #
    #     result['city'] = city
    #     result['status'] = True
    #     result['msg'] = "Contact to owner of ad  has save successfully"
    #     return Response(result, status=status.HTTP_200_OK)