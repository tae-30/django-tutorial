import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Event(models.Model):
    event_name = models.CharField(max_length=5)


class Date(models.Model):
    date = models.DateField()
    time = models.TimeField()


class Note(models.Model):
    note = models.CharField(max_length=300)
