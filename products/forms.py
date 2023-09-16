from django import forms
from .models import *



class CommentForm(forms.ModelForm):


    class Meta:
        model = Comments
        fields = ['which_post', 'name', 'email', 'message']


class ReplayForm(forms.ModelForm):


    class Meta:
        model = Replay
        fields = ['which_comment', 'message']