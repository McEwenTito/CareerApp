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


#fix this
class Prerequisite(models.Model):
    subject = models.ForeignKey('Subject')
    points = models.IntegerField(default=6)


    def __str__(self):
        return self.subject.name

class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CareerPathway(models.Model):
    name = models.CharField(max_length=200)
    cluster = models.ForeignKey('CareerCluster', null=True)

    def __str__(self):
        return self.name

class Programme(models.Model):
    name = models.CharField(max_length=500)
    faculty = models.ForeignKey('Faculty')
    duration = models.IntegerField(default=4)
    prereq = models.ManyToManyField(Subject, null=True, blank=True)
    career = models.ManyToManyField(CareerPathway, blank=True)

    def __str__(self):
        return self.name



class CareerCluster(models.Model):
    name = models.CharField(max_length=200)
    programme = models.ManyToManyField('Programme')
    info = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

class ClusterActivity(models.Model):
    activity = models.TextField()
    cluster = models.ForeignKey('CareerCluster')

    def __str__(self):
        return self.activity
