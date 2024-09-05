from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
import random

class CustomUserManager(BaseUserManager):
  def create_user(self, username, email, phone=None, password=None, **extra_fields):
    if not email:
      raise ValueError('The Email field must be set')
    email = self.normalize_email(email)
    user = self.model(username=username, email=email, phone=phone, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, username, email,  password=None, **extra_fields):
    phone = input("Phone number: ") 

    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')
    
    return self.create_user(username, email, phone, password, **extra_fields)

class User(AbstractUser):
  email = models.EmailField(unique=True)
  phone = models.IntegerField("Номер телефона", unique=True)
  balance = models.DecimalField("Баланс", max_digits=10, decimal_places=2, default=0.00)
  account = models.BigIntegerField(editable=False)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def save(self, *args, **kwargs):
    if not self.pk:
      self.account = f'103012{random.randint(1000000000, 9999999999)}'

    super().save(*args, **kwargs)

  def __str__(self):
    return self.username

