from django.db import models

# Create your models here.
class Data(models.Model):
    date = models.DateTimeField("Дата", auto_now_add=True, max_length=19, null=False, unique=True)
    temperature = models.FloatField("Температура", null=True)
    humidity = models.FloatField("Влажность", null=True)
