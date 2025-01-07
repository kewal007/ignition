from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

#custom user model that stores the user data
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) 
    username = models.CharField(max_length=150, unique=True)  
    password=models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    #configuring the project to use custom user model instead of django's default user model
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # This is a unique name to prevent clash
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Unique related name to prevent clash
        blank=True
    )
    
    #return the name of the user when the user object is created
    def __str__(self):
        return self.username
