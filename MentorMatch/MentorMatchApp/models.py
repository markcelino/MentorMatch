from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class ExamplePerson(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    age = models.IntegerField()

    #This is one way to handle relationships between entities
    interests = models.ManyToManyField("ExampleInterests")

    # This is how the object displays if we print it
    def __unicode__(self):
        return self.name 
        # Example of what unicode does:
        # --> michaelObject.name = "Michael Willingham"
        # --> print michaelObject
        # michael willingham

class ExampleInterests(models.Model):
    interest_name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.interest_name
