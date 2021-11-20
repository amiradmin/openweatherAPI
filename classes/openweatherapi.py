import requests

class OpenWeather:
    api_key = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d0e239f15d5f56006808fd1cf63f968c'

    def getWeather(self,city):
        print("Inside")
        result = requests.get(self.api_key.format(city)).json()
        return result