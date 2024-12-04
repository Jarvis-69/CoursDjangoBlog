from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Sélectionnez une catégorie",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Choisir une catégorie'
        })
    )
    
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Titre de l\'article'
        })
    )
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 8,
            'placeholder': 'Contenu de l\'article'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']