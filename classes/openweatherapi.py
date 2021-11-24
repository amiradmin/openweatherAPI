import requests
import os

class OpenWeather:
    api_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d0e239f15d5f56006808fd1cf63f968c'

    def getWeather(self,city):
        print("Inside")
        result = requests.get(self.api_link.format(city)).json()
        return result


if __name__ == '__main__':
    from os import sys, path
    obj = OpenWeather()
    print(obj.getWeather("Tehran"))
