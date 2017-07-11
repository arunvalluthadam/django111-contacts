from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator



# Create your models here.
class Contacts(models.Model):
 user = models.ForeignKey(settings.AUTH_USER_MODEL)
 first_name = models.CharField(max_length=30)
 last_name = models.CharField(max_length=30)
 phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
 phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)
 email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
 favourite = models.BooleanField(default=False)

 def __str__(self):              # __unicode__ on Python 2
    return self.first_name 
