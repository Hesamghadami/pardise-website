from django import forms
from .models import *


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'telephone','email', 'subject', 'message']