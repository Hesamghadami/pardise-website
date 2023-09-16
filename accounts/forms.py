from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import CustumUser



class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField()


    class Meta:
        model = CustumUser
        fields = ['username', 'password1', 'password2', 'email', 'image']