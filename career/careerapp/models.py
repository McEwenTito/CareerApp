from django.db import models
from django.utils import timezone

class School(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey('School')

    def __str__(self):
        return self.name

class Programme(models.Model):
    name = models.CharField(max_length=500)
    faculty = models.ForeignKey('Faculty')

    def __str__(self):
        return self.name

class Career(models.Model):
    name = models.CharField(max_length=200)
    programme = models.ForeignKey('Programme')

    def __str__(self):
        return self.name
