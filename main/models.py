from django.db import models

class News(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
