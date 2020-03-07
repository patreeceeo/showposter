# posts/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = [ 'created_by' ]
        fields = ['image', 'date_of_show', 'alternate_text']
        widgets = {
            'image': forms.HiddenInput
        }
