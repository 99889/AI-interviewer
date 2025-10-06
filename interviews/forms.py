from django import forms
from .models import Candidate

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['resume']

class MissingFieldsForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'email', 'phone']
