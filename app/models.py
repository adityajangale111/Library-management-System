from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 



class Book_type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Language(models.Model):
    lang = models.CharField(max_length=50)

    def __str__(self):
        return self.lang


class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length=100)
    language = models.ForeignKey(Language,on_delete=models.CASCADE) 
    img = models.ImageField(upload_to = 'book')

    def __str__(self):
        return self.title



def create_user(sender, *args, **kwargs):
    if kwargs['created']:
        user = User.objects.create(username=kwargs['instance'],password="welcome")

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10,unique=True)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=10,unique=True)
    total_books_due = models.IntegerField(default=0)
    img = models.ImageField(upload_to = 'profile')

    def __str__(self):
        return self.roll_no



class Person(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=100)
    Type = models.CharField(max_length=50,blank=True)
    Language = models.CharField(max_length=100)
    Summary = models.CharField(max_length=500)
    Total_copies = models.CharField(max_length=50)
    Available_copies =models.CharField(max_length=50)
    