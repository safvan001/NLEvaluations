
# models.py

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)



class AndroidApp(models.Model):
    CATEGORY_CHOICES = (
        ('Entertainment', 'Entertainment'),
        ('Utility', 'Utility'),
        ('Others', 'Others'),
        # Add more categories as needed
    )

    SUBCATEGORY_CHOICES = (
        ('Social Media', 'Social Media'),
        ('Media Player', 'Media Player'),
        ('Gamming', 'Gamming'),

        # Add more subcategories as needed
    )

    name = models.CharField(max_length=100)
    points = models.PositiveIntegerField()
    image = models.ImageField(upload_to='img/app_images',null=True, blank=True)  # Example: Use ImageField for image upload
    link = models.URLField(default='https://default-link.com')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default='1')
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES,default='1')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='img/profile_images', null=True, blank=True)
    points_earned = models.PositiveIntegerField(default=0)

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='img/task_screenshots', null=True, blank=True)
