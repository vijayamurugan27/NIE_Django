from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    departent = models.CharField(max_length=10)
    rollnumber = models.IntegerField()
    def __str__(self):
        return self.name