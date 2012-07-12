from django import forms
from models import *

#This is how we create a form... (Insert Win button here)
class Example_Person_Form(forms.ModelForm):
    class Meta:
        model = CustomUser
        #Fields we don't want the user to edit on the form
        exclude = ('address')

class Login(forms.Form):
    alias = forms.CharField(max_length=4)
    password = forms.CharField(widget=forms.PasswordInput)
