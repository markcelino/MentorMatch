from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, UserManager

# Create your models here.

class CustomUser(User):
    """User with app settings."""
    name = models.CharField(max_length=250)
#   email = models.CharField(max_length=250)
    department = models.CharField(max_length=250)      
    mentee = models.BooleanField()
    mentor = models.BooleanField()
    numMentees = models.IntegerField()
    numMentors = models.IntegerField()

    #This is one way to handle relationships between entities
    interests = models.ManyToManyField("Interest")
    campus = models.ForeignKey('Campus')
    building = models.ForeignKey('Building')

    mentors = models.ManyToManyField("CustomUser", related_name='MentorOf', blank=True)
    mentees = models.ManyToManyField('CustomUser', related_name='MenteeOf', blank=True)
        
    # This is how the object displays if we print it
    def __unicode__(self):
        return self.name 
        # Example of what unicode does:
        # --> michaelObject.name = "Michael Willingham"
        # --> print michaelObject
        # michael willingham

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()

    def check_password(self, password):
        if (self.password == password):
            return True
        return False
"""
class User(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    age = models.IntegerField()

    #This is one way to handle relationships between entities
    interests = models.ManyToManyField("Interests")

    # This is how the object displays if we print it
    def __unicode__(self):
        return self.name 
        # Example of what unicode does:
        # --> michaelObject.name = "Michael Willingham"
        # --> print michaelObject
        # michael willingham
"""
class Interest(models.Model):
    interest_name = models.CharField(max_length=250,primary_key=True)
    expertise = models.BooleanField()

    users = models.ManyToManyField("CustomUser", blank=True)    
    
    def __unicode__(self):
        return self.interest_name

class Campus(models.Model):
    campus_name = models.CharField(max_length=250,primary_key=True)

    def __unicode__(self):
        return self.campus_name

class Building(models.Model):
    building_name = models.CharField(max_length=250,primary_key=True)

    campus = models.ForeignKey('Campus')

    def __unicode__(self):
        return self.building_name

