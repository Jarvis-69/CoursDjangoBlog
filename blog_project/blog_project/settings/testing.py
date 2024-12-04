from .base import *

DEBUG = False
ALLOWED_HOSTS = []

# Base de données pour les tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_db',
        'USER': 'postgres',
        'PASSWORD': 'nhoss69N',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Désactiver les restrictions de mot de passe
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Backend email simulé
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
