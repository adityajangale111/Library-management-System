from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User   
        fields =["username","Roll_no","password1","password2",'email']
    username = forms.CharField()
    Roll_no = forms.CharField(max_length=10)
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    email = forms.EmailField()


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"




class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"