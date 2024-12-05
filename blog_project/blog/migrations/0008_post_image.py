# blog/migrations/0008_post_image.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_options_alter_category_name_and_more'),
    ]

    operations = [
        # Supprimez cette ligne si la colonne existe déjà
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts/', null=True, blank=True),
        ),
    ]
