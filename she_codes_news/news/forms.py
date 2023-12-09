from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm): #inherits from ModelForm class to create a new type. Does the bulk of creating a form for you. 
    class Meta: 
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder': 'Select a date',
                    'type':'date'
                }
            )
        }