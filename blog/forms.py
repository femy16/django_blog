from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['author','views']
        # fields= '__all__'