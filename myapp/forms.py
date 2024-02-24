from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddNoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['title', 'body']
    widgets = {
      'body': forms.Textarea(attrs={'rows': 8, 'resize': 'none', 'class': 'form-control', 'placeholder': 'Enter the body of your Note'}),
      'title': forms.TextInput(attrs={'placeholder': 'Enter the title of your Note', 'class': 'form-control'})
    }

class SignUpForm(UserCreationForm):
  password1 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'placeholder':'Enter your password'}),
  )
  password2 = forms.CharField(
    label="Confirm password",
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'placeholder':'Confirm your password'}),
  )

  email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}))

  class Meta:
    model = User
    fields = ['email', 'username', 'password1', 'password2']
    widgets = {
      'username': forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
    }