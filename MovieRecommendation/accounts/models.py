from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio=models.TextField(max_length=500,blank=True,null=True)
    profile_picture=models.ImageField(upload_to='profile_pictures',blank=True,null=True)

    groups=models.ManyToManyField('auth.Group',blank=True,related_name='customuser_set',)

    user_permissions=models.ManyToManyField('auth.Permission',blank=True)

    def __str__(self):
        return self.username