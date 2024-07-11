from django.db import models

# Create your models here.
class Program(models.Model):
    header = models.CharField(max_length=50)
    users = models.CharField(max_length=10, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    link = models.TextField()

class Event(models.Model):
    image = models.ImageField(upload_to='static/uploads/')
    header = models.CharField(max_length=100)
    paragraph = models.CharField(max_length=255)
    link = models.TextField(null=True, blank=True)

class Subscriber(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True, blank=True)