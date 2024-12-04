# Generated by Django 5.1.3 on 2024-12-04 21:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'permissions': [('can_publish_post', 'Peut publier un article'), ('can_feature_post', 'Peut mettre en avant un article')], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, help_text="Indique si l'article est publié et visible", verbose_name='Publié'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Dernière modification'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Nom de la catégorie (100 caractères maximum)', max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, help_text='URL conviviale générée automatiquement à partir du nom', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text="Auteur de l'article", on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(help_text="Catégorie de l'article", on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category', verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text="Contenu de l'article en format texte", verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, help_text='URL conviviale générée automatiquement à partir du titre', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text="Titre de l'article (200 caractères maximum)", max_length=200, verbose_name='Titre'),
        ),
    ]
