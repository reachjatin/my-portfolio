from django.db import models

# Create your models here.

class Skills(models.Model):
    skillname = models.CharField(max_length=255)
    percentage = models.IntegerField()

    def __str__(self):
        return self.skillname

class Portfolio(models.Model):
    projectpic = models.ImageField(upload_to='images/')
    projecttitle = models.CharField(max_length=255)
    projectsummary = models.TextField()
    projectDescription = models.TextField()

    def __str__(self):
        return self.projecttitle

class Person(models.Model):
    name = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skills)
    portfolios = models.ManyToManyField(Portfolio)
    title = models.TextField()
    dob = models.DateField()
    email = models.EmailField(max_length=30)
    phoneNo = models.BigIntegerField()
    address = models.TextField()
    languages = models.TextField()
    description = models.TextField()
    profilepic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
