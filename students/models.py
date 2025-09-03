from django.db import models



class Course(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    course = models.ManyToManyField(Course, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=500)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name






