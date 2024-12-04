from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    """
    Modèle représentant une catégorie d'articles dans le blog.
    """
    name = models.CharField(max_length=100, verbose_name="Nom")
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        print(f"Saving Category: {self.name}")
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Post(models.Model):
    """
    Modèle représentant un article du blog.
    """
    title = models.CharField(max_length=200, verbose_name="Titre")
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='posts', 
        verbose_name="Auteur"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='posts', 
        verbose_name="Catégorie"
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name="Publié")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def save(self, *args, **kwargs):
        print(f"Saving Post: {self.title}")
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
