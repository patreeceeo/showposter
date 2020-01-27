# posts/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'end_date', 'alternate_text', 'full_size']
        widgets = {
            'image': forms.HiddenInput
        }
