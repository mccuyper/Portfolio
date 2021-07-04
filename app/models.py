from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MyPersonalData(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30, default='Available')
    Address = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Skype = models.CharField(max_length=30)
    Languages = models.CharField(max_length=80)


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=40, default="")
    content = models.TextField()
    technologies =  models.CharField(max_length=20, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    yourName = models.CharField(max_length=20)
    yourEmail = models.CharField(max_length=40)
    yourSubject = models.CharField(max_length=20)
    ourMessage = models.TextField()


class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    project = models.TextField()
    client = models.CharField(max_length=20)
    preview = models.CharField(max_length=30)
    languages = models.TextField()

    def __str__(self):
        return self.title
