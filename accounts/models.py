# coding: utf-8

from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from core.models import AbstractBaseModel
from django.db import models

# Create your models here.


class User(AbstractUser, AbstractBaseModel):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
        ('common', 'Common'),
    )

    phone_number = models.CharField(blank=True, max_length=15)
    token = models.CharField(null=True, max_length=255)
    role = models.CharField(choices=ROLE_CHOICES, max_length=32)

