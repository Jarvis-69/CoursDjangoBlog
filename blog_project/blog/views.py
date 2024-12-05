import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.i18n import set_language
from .models import Post, Category
from .forms import PostForm, RegisterForm
from django.db.models import Count
from django.http import JsonResponse

logger = logging.getLogger('blog')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info(f'{_("New user registered")}: {user.username}')
            messages.success(request, _('Account created successfully!'))
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# def post_list(request):
#     posts = Post.objects.all().select_related('author', 'category')
#     categories = Category.objects.all()
#     return render(request, 'blog/post_list.html', {
#         'posts': posts,
#         'categories': categories
#     })

def post_list(request):
    posts = Post.objects.all().select_related('author', 'category')
    categories = Category.objects.all()
    # Ajoutez une liste avec l'état "favori" pour chaque post
    posts_with_favorites = []
    for post in posts:
        is_favorited = request.user.is_authenticated and post.favorites.filter(id=request.user.id).exists()
        posts_with_favorites.append({
            'post': post,
            'is_favorited': is_favorited,
        })
    return render(request, 'blog/post_list.html', {'posts_with_favorites': posts_with_favorites})

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related('author', 'category'), slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, _('Post created successfully!'))
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        messages.error(request, _("You don't have permission to edit this post"))
        return redirect('post_detail', slug=slug)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, _('Post updated successfully!'))
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        messages.error(request, _("You don't have permission to delete this post"))
        return redirect('post_detail', slug=slug)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, _('Post deleted successfully!'))
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post': post})

def logout_view(request):
    logout(request)
    messages.success(request, _('You have been logged out successfully.'))
    return redirect('post_list')

def filter_by_category(request, name=None):
    # Ajouter un compteur d'articles pour chaque catégorie
    categories = Category.objects.annotate(post_count=Count('posts'))

    if name:  # Vérifie si un nom de catégorie est passé
        category = get_object_or_404(Category, name=name)
        posts = Post.objects.filter(category=category, is_published=True)
        current_category = category
    else:
        posts = Post.objects.filter(is_published=True)
        current_category = None

    return render(request, 'blog/filter_by_category.html', {
        'categories': categories,
        'posts': posts,
        'current_category': current_category,
    })

@login_required
def toggle_favorite(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.favorites.filter(id=request.user.id).exists():
        post.favorites.remove(request.user)
        status = "removed"
    else:
        post.favorites.add(request.user)
        status = "added"
    return JsonResponse({"status": status, "favorites_count": post.favorites.count()})

