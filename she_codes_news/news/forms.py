from django import forms
from django.forms import ModelForm
from .models import NewsStory

#inherits from ModelForm class to create a new type. Does the bulk of creating a form for you. 
class StoryForm(ModelForm): 
    class Meta: 
        model = NewsStory
        fields = ['title', 'pub_date','tag_line','category', 'story_image_URL', 'content']
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
    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'