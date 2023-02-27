from .models import *
from django import forms

class authorForm(forms.ModelForm):
    fname = forms.CharField(max_length = 200, help_text='Enter First Name: ')
    lname = forms.CharField(max_length = 200, help_text='Enter Last Name: ')
    email = forms.CharField(max_length = 200, help_text='Enter Email: ')
    class Meta:
        model = Author
        fields = '__all__'
        exclude = ['created']

