from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'created_at')
   search_fields = ['name']
   list_per_page = 20

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'category', 'created_at')
   list_filter = ('category', 'created_at')
   search_fields = ('title', 'content')
   prepopulated_fields = {'slug': ('title',)}

   def formfield_for_foreignkey(self, db_field, request, **kwargs):
       if db_field.name == "category":
           kwargs["queryset"] = Category.objects.order_by('name')
       return super().formfield_for_foreignkey(db_field, request, **kwargs)