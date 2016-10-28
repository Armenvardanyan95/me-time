# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from accounts.models import User

from core.models import AbstractBaseModel

DAYS_OF_WEEK = (
    ('monday', 'Երկուշաբթի'),
    ('tuesday', 'Երեքշաբթի'),
    ('thursday', 'Չորեքշաբթի'),
    ('wednesday', 'Հինգշաբթի'),
    ('thursday', 'Ուրբաթ'),
    ('saturday', 'Շաբաթ'),
    ('sunday', 'Կիրակի'),
)

class PlaceType(AbstractBaseModel):
    type_title = models.CharField(max_length=64)

class Place(models.Model):
    title = models.CharField(max_length=50, blank=False)
    place_type = models.ManyToManyField(PlaceType)
    address = models.CharField(max_length=250, blank=False)
    admin = models.OneToOneField(User)
    coordinates = models.CharField(max_length=250, blank=False)
    phone = models.CharField(max_length=30, blank=False)
    work_hours_begin = models.TimeField()
    work_hours_end = models.TimeField()
    force_close = models.BooleanField(default=False)
    work_days_begin = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    work_days_end = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    main_pic = models.ImageField(upload_to='places/')
    logo = models.ImageField(upload_to='places/')
    description = models.TextField(max_length=1000)
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Place, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



