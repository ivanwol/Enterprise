from django.db import models


class Chicken(models.Model):
    weight = models.PositiveSmallIntegerField()
    date = models.CharField(max_length=20)


