from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(max_length=300)
    phone_no = models.CharField(max_length=15)
    summary = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    linkedin = models.CharField(max_length=300, blank=True)
    github = models.CharField(max_length=300, blank=True)
    website = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.email
