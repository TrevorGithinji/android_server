from django.db import models

# Create your models here.

class Person(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    edu_level = models.CharField(max_length=100)
    class Meta:
        db_table = 'watu'

