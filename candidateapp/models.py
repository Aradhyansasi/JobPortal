from django.db import models
from usersapp.models import User
# Create your models here.

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidates')
    pro_pic = models.ImageField(upload_to='profiles')
    qualification = models.CharField(max_length=120)
    age = models.PositiveIntegerField(default=17)
    skills = models.CharField(max_length=120, null=True)
    cv = models.FileField(upload_to='cvs', null=True)
