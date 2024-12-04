import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Post, Category
from .forms import PostForm

logger = logging.getLogger('blog')

def post_list(request):
    logger.info('Accès à la liste des articles')
    posts = Post.objects.select_related('author', 'category').all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related('author', 'category'), slug=slug)
    logger.info(f'Consultation de l\'article: {post.title}')
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            logger.info(f'Nouvel article créé: {post.title} par {request.user.username}')
            messages.success(request, 'Article créé avec succès!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'action': 'new'})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        logger.warning(f'Tentative de modification non autorisée de l\'article {post.title} par {request.user.username}')
        messages.error(request, "Vous n'avez pas la permission de modifier cet article")
        return redirect('post_detail', slug=slug)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            logger.info(f'Article modifié: {post.title} par {request.user.username}')
            messages.success(request, 'Article modifié avec succès!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'action': 'edit', 'post': post})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        logger.warning(f'Tentative de suppression non autorisée de l\'article {post.title} par {request.user.username}')
        messages.error(request, "Vous n'avez pas la permission de supprimer cet article")
        return redirect('post_detail', slug=slug)
    
    if request.method == "POST":
        title = post.title
        post.delete()
        logger.info(f'Article supprimé: {title} par {request.user.username}')
        messages.success(request, 'Article supprimé avec succès!')
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post': post})

def logout_view(request):
    username = request.user.username
    logout(request)
    logger.info(f'Utilisateur {username} déconnecté')
    return redirect('post_list')