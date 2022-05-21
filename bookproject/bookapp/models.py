from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from bookapp.manager import CustomUserManager
# Create your models here.

class Book_detail(models.Model):
    author_name=models.CharField(max_length=150)
    author_publisheddate=models.DateField(auto_now=True)
    bookname=models.CharField(max_length=150)
    book_filename=models.CharField(max_length=150)


class MyUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(('email_address'),unique=True)
    name=models.CharField(blank=True,max_length=255)
    contact=models.CharField(blank=True,max_length=255)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','contact']
    objects=CustomUserManager()
    def __str__(self):
        return self.email