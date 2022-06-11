from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
   phone = models.CharField(max_length=12)
   options = (
       ('employer', 'employer'),
       ('candidate', 'candidate')
   )
   role= models.CharField(max_length=12, choices=options, default='candidate')

   @property
   def is_candidate(self):
     return self.role=='candidate'

   @property
   def is_employer(self):
     return self.role=='employer'