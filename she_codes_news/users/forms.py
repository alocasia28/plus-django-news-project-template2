from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta: 
        model = CustomUser
        fields = ['username','email']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'    
                  
class CustomUserChangeForm(UserChangeForm):
    class Meta: 
        model = CustomUser
        fields = ['username','email']