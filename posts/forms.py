from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "placeholder": "Write a comment...",
                "rows": 2,
                "class": "form-control",
            }),
        }