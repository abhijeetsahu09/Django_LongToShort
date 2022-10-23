from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
class LongToShort(models.Model):
    long_url = models.URLField(max_length = 500)
    short_url = models.CharField(max_length = 50, unique = True)
    date = models.DateTimeField(auto_now_add = True)
    clicks = models.IntegerField(default = 0)

class details(models.Model):
    country = models.CharField(max_length = 50, unique = True)
    state = models.CharField(max_length = 10)
    city = models.CharField(max_length = 10)