from candidateapp.models import CandidateProfile
from django import forms

class CandProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        exclude = ('user',)
