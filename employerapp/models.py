from django.db import models
from usersapp.models import User
# Create your models here.

class EmployerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='employer')
    company_name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='images')
    bio = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    services = models.CharField(max_length=120)


class Jobs(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company')
    job_title = models.CharField(max_length=120)
    job_description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title


class Applications(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applicants')
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, related_name='jobtype')
    options = (
        ('applied', 'applied'),
        ('rejected', 'rejected'),
        ('pending', 'pending'),
        ('cancelled', 'cancelled'),
        ('accepted', 'accepted')
    )
    status = models.CharField(max_length=50, choices=options, default='applied')
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (
            'applicant', 'job'
        )


