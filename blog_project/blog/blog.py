from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    list_per_page = 20

    def post_count(self, obj):
        """Return the number of posts associated with a category."""
        return obj.posts.count()
    post_count.short_description = "Nombre d'articles"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'status_display')
    list_filter = ('category', 'created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    list_per_page = 20
    readonly_fields = ('created_at',)

    def status_display(self, obj):
        """Show a status indicator for published posts."""
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            '#28a745' if obj.pk else '#dc3545',
            '✓ Publié' if obj.pk else '⨉ Non publié'
        )
    status_display.short_description = 'Statut'

    def save_model(self, request, obj, form, change):
        """Automatically assign the logged-in user as the author of a new post."""
        if not obj.pk:  # If it's a new object
            obj.author = request.user
        super().save_model(request, obj, form, change)
