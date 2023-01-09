from django import forms
from django.contrib.auth.models import User

from comments.models import Comment

class NewCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write a comment'}), required=True)
    
    class Meta:
        model = Comment
        fields = ("body",)