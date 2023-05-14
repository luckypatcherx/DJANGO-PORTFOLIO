from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    skill_category = forms.ModelChoiceField(queryset=Skill.objects.values_list('skill_category', flat=True).distinct())
    
    class Meta:
        model = Skill
        fields = ['skill_category', 'skill_name', 'rating']