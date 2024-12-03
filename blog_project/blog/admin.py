from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')  # Colonnes affichées
    prepopulated_fields = {'slug': ('title',)}  # Génération automatique du slug
