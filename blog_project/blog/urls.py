from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Liste des articles
    path('post/new/', views.post_new, name='post_new'),  # Création d'un article
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Détails d'un article
]