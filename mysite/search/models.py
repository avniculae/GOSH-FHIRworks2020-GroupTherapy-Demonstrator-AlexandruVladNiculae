from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patients(models.Model):
    uuid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = 'Patients'