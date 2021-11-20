from django.db import models

# Create your models here.
class Weather(models.Model):

    city = models.CharField(max_length=512,null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city