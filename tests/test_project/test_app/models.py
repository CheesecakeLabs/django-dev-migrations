from django.db import models


class TestModel(models.Model):
    field_1 = models.CharField(max_length=10, null=True)
    field_2 = models.IntegerField()
