from django.test import RequestFactory, TestCase
from weather.models import Weather
import datetime


class SimpleTest(TestCase):  # type: Type[TestCase]
    """
    Ensure we can insert data to database.
    """
    def setUp(self):  # type: SimpleTest
        self.factory = RequestFactory()

    def test_database_insertion(self):  # type: SimpleTest
        obj = Weather()
        obj.city = 'tehranTest'
        obj.temperature = '10.24'
        obj.datetime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        obj.save()
        self.assertTrue(obj)
