Blog Django
Ce projet est un blog développé avec Django permettant la gestion d'articles et de catégories.
Fonctionnalités

Gestion des articles (CRUD)
Système de catégories
Authentification utilisateur
Interface d'administration
Système de logging
URLs conviviales avec slugs
Design responsive

Prérequis

Python 3.12+
PostgreSQL
pip
virtualenv

Installation

Clonez le répertoire

 
cd blog_project

Créez un environnement virtuel et activez-le

bashCopypython -m venv env
source env/bin/activate  # Sur Unix
env\Scripts\activate  # Sur Windows

Installez les dépendances

bashCopypip install -r requirements.txt

Configurez la base de données PostgreSQL dans settings.py

pythonCopyDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Effectuez les migrations

bashCopypython manage.py makemigrations
python manage.py migrate

Créez un superutilisateur

bashCopypython manage.py createsuperuser

Lancez le serveur

bashCopypython manage.py runserver
Structure du Projet
Copyblog_project/
├── blog/
│   ├── migrations/
│   ├── templates/blog/
│   │   ├── base.html
│   │   ├── post_list.html
│   │   ├── post_detail.html
│   │   └── post_edit.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/
│   └── images/
├── manage.py
└── requirements.txt
Utilisation
Administration

Accédez à /admin pour gérer les articles et catégories
Créez des catégories avant de créer des articles

Gestion des Articles

Liste des articles : /
Création d'article : /post/new/
Détail d'un article : /post/<slug>/
Modification : /post/<slug>/edit/
Suppression : /post/<slug>/delete/

Logs
Les logs sont configurés pour enregistrer :

Les accès aux articles
Les créations/modifications/suppressions
Les tentatives d'accès non autorisées

Contribution

Fork le projet
Créez une branche (git checkout -b feature/AmazingFeature)
Committez vos changements (git commit -m 'Add some AmazingFeature')
Push vers la branche (git push origin feature/AmazingFeature)
Ouvrez une Pull Request

License
Ce projet est sous licence MIT.
Contact

mohamed.djabi@outlook.fr