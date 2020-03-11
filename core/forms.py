from django import forms

from .models import Snippet, Tag

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('title', 'user', 'description', 'language', 'code')