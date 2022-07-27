from django.db import models


class Feed(models.Model):
    producer = models.CharField(max_length=20)
    weight_feed = models.PositiveSmallIntegerField()
    price = models.FloatField()