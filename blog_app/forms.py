from django import forms
from blog_app.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        