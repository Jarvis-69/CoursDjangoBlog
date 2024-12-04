import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import Post, Category
from .forms import PostForm, RegisterForm

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
            logger.info(f'Nouvel utilisateur inscrit: {user.username}')
            messages.success(request, 'Compte créé avec succès!')
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().select_related('author', 'category')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories
    })

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
            messages.success(request, 'Article créé avec succès!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        messages.error(request, "Vous n'avez pas la permission de modifier cet article")
        return redirect('post_detail', slug=slug)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Article modifié avec succès!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        messages.error(request, "Vous n'avez pas la permission de supprimer cet article")
        return redirect('post_detail', slug=slug)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Article supprimé avec succès!')
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post': post})

def logout_view(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('post_list')