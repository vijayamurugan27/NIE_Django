from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    rollno = models.IntegerField(default= 6100)
    def __str__(self):
        return self.name