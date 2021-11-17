from django.db import models

class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=50)
    marks = models.IntegerField()

