from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Kharj(models.Model):

    tozihat = models.TextField()

    tarikh = models.DateTimeField()

    meghdar_kharj = models.BigIntegerField()

    user = models.ForeignKey(User,on_delete=models.CASCADE)           # کسی که خرج را انجام داده است


