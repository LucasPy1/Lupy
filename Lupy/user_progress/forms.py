from django import forms
from .models import SkillModel

class SkillForm(forms.ModelForm):
    class Meta:

        model = SkillModel
        fields = ['name', 'description']  # I removed level because i want the default value of 1