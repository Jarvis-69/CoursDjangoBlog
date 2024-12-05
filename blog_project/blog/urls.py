from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Liste des articles
    path('post/new/', views.post_new, name='post_new'),  # Nouvelle publication
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Détail d'un article
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),  # Édition d'un article
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),  # Suppression d'un article
    path('categories/', views.filter_by_category, name='filter_by_category'),  # Tous les articles
    path('categories/<str:name>/', views.filter_by_category, name='filter_by_category_name'),  # Articles d'une catégorie spécifique
    path('toggle-favorite/<int:post_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Connexion
    path('logout/', views.logout_view, name='logout'),  # Déconnexion
    path('register/', views.register_view, name='register'),  # Inscription
]
