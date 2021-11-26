import requests


class OpenWeather:
    """
    We get response from OpeWeather webservice.
    """
    api_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d0e239f15d5f56006808fd1cf63f968c'

    def getWeather(self,city): # type: OpenWeather  # type: (str) -> str
        """

        Args:
            city (string):
        """
        result = requests.get(self.api_link.format(city)).json()
        return result


