from django import forms
from employerapp.models import EmployerProfile, Jobs

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        exclude = ('user',)


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude = ('posted_by','posted_date')
