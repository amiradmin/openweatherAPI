from django.test import RequestFactory, TestCase
from weather.models import Weather
import datetime


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        weather = Weather.objects.create(
            city='tehranTest', temperature='11.20', datetime=datetime.datetime.now())

    def test_something_that_will_fail(self):
        obj = Weather()
        obj.city = 'tehranTest'
        obj.temperature = '10.24'
        obj.datetime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        obj.save()
        self.assertTrue(obj)
