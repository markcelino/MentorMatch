from django import forms
from models import *

#This is how we create a form... (Insert Win button here)
class Example_Person_Form(forms.ModelForm):
    class Meta:
        model = CustomUser
        #Fields we don't want the user to edit on the form
        exclude = ('address','is_staff','is_active','is_superuser','last_login','first_name','last_name')

