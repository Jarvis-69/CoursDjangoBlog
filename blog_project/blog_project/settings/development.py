from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Base de données pour le développement
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'postgres',
        'PASSWORD': 'nhoss69N',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Fichiers statiques pour le développement
STATICFILES_DIRS = [BASE_DIR / "static"]
