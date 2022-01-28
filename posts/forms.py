from django.contrib.auth.forms import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget,SummernoteInplaceWidget


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','body','tags')
        widgets = {'body': SummernoteWidget()}