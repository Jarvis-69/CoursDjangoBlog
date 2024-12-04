from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from django.urls import reverse
from .models import Post, Category

# Ajout de logs pour vérifier que `admin.py` est chargé
print("Admin.py chargé avec succès")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Configuration de l'administration pour les catégories.
    """
    list_display = ('name', 'slug', 'post_count', 'display_status')  # Colonnes visibles
    search_fields = ('name',)  # Barre de recherche
    prepopulated_fields = {'slug': ('name',)}  # Génération automatique du slug
    ordering = ['name']  # Tri alphabétique
    list_per_page = 20  # Pagination des résultats

    fieldsets = (
        (None, {
            'fields': ('name', 'slug'),
        }),
        ('Méta-informations', {
            'classes': ('collapse',),
            'fields': (),
            'description': 'Informations générées automatiquement'
        }),
    )

    def post_count(self, obj):
        """
        Retourne le nombre d'articles dans la catégorie avec un lien vers les articles.
        """
        count = obj.posts.count()
        if count:
            return format_html(
                '<a href="{}?category__id__exact={}">{} article{}</a>',
                reverse('admin:blog_post_changelist'),
                obj.id,
                count,
                's' if count > 1 else ''
            )
        return '0 article'
    post_count.short_description = "Nombre d'articles"

    def display_status(self, obj):
        """
        Affiche un indicateur visuel du statut de la catégorie.
        """
        count = obj.posts.count()
        if count > 0:
            return format_html(
                '<span style="color: #28a745;">✓ Active ({} article{})</span>',
                count, 's' if count > 1 else ''
            )
        return format_html('<span style="color: #dc3545;">○ Vide</span>')
    display_status.short_description = "Statut"

    def get_queryset(self, request):
        """
        Optimise les requêtes en ajoutant le compte des articles.
        """
        queryset = super().get_queryset(request)
        return queryset.annotate(post_count=Count('posts'))


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuration de l'administration pour les articles.
    """
    list_display = ('title', 'author', 'category_link', 'created_at', 'is_published', 'status_display')
    list_filter = ('category', 'is_published', 'created_at')  # Filtres latéraux
    search_fields = ('title', 'content')  # Barre de recherche
    prepopulated_fields = {'slug': ('title',)}  # Génération automatique du slug
    raw_id_fields = ('author',)  # Champ auteur avec recherche rapide
    date_hierarchy = 'created_at'  # Navigation par date
    list_per_page = 20  # Pagination
    readonly_fields = ('created_at',)  # Champ en lecture seule

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content')
        }),
        ('Attribution', {
            'fields': ('author', 'category'),
            'description': 'Informations sur l\'auteur et la catégorie'
        }),
        ('Métadonnées', {
            'classes': ('collapse',),
            'fields': ('created_at',),
        }),
    )

    def category_link(self, obj):
        """
        Affiche la catégorie avec un lien vers sa page d'édition.
        """
        if obj.category:
            return format_html(
                '<a href="{}">{}</a>',
                reverse('admin:blog_category_change', args=[obj.category.id]),
                obj.category.name
            )
    category_link.short_description = 'Catégorie'

    def status_display(self, obj):
        """
        Affiche le statut de l'article avec un indicateur visuel.
        """
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            '#28a745' if obj.is_published else '#dc3545',
            '✓ Publié' if obj.is_published else '⨉ Non publié'
        )
    status_display.short_description = 'Statut'

    def save_model(self, request, obj, form, change):
        """
        Attribue automatiquement l'auteur lors de la création.
        """
        if not obj.pk:  # Si c'est un nouvel article
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Post)