from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Sélectionnez une catégorie"
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']