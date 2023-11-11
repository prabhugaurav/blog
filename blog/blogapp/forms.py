from django import forms
from blogapp.models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Django Form
class StudentFormClass(forms.Form):
    name=forms.CharField()
    roll_number=forms.IntegerField()
    percentage=forms.FloatField()
# Model From
class StudentModelFormClass(forms.ModelForm):
    name=forms.CharField()
    roll_number=forms.IntegerField()
    per=forms.FloatField()
    class Meta:
        model=Student
        fields=['name','rno','per']

class UserRegister(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
