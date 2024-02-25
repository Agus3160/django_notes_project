from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import User

class AddNoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['title', 'body']
    widgets = {
      'body': forms.Textarea(attrs={'rows': 8, 'style': 'resize: none;', 'class': 'form-control', 'placeholder': 'Enter the body of your Note'}),
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

  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
    widgets = {
      'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control', 'required': True}),
      'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control', 'required': True}),
      'username': forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control', 'required': True}),
      'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control', 'required': True})
    }

class LoginForm(forms.Form):
  username= forms.CharField(
    widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
    max_length= 150,
    label="Username",
    min_length=5,
    required=True
  )
  
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'placeholder':'Enter your password'}),
    label="Password",
    required=True
  )


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
      email = self.cleaned_data['email']
      if not User.objects.filter(email=email).exists():
        raise forms.ValidationError("There is no user with that email address.")
      return email
