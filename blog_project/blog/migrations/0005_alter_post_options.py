# Generated by Django 5.1.3 on 2024-12-04 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]