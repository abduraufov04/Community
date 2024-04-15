from django import forms
from .models import Blog
from django_summernote.widgets import SummernoteWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['img', 'title', 'type', 'body']
        widgets = {'body': SummernoteWidget()}
        
    def create(self, validated_data):
        print(1111111, validated_data)
        
        return super().create(validated_data)