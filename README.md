
  

  
# Blog Django

Ce projet est un blog développé avec Django, permettant la gestion d'articles et de catégories.

## Fonctionnalités

- **Gestion des articles** (CRUD)
- **Système de catégories**
- **Authentification utilisateur**
- **Interface d'administration**
- **Système de logging**
- **URLs conviviales avec slugs**
- **Design responsive**

## Prérequis

- [Python 3.12+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- `pip`
- `virtualenv`

## Installation

1. **Clonez le répertoire :**

   ```  
   git clone https://github.com/nhoss6/CoursDjangoBlog.git
   cd CoursDjangoBlog
Créez un environnement virtuel et activez-le :
  

  
python -m venv env
# Sur Unix
source env/bin/activate
# Sur Windows
env\Scripts\activate
Installez les dépendances :
  

  
pip install -r requirements.txt
Configurez la base de données PostgreSQL dans settings.py :
python

Exécuter

  
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Effectuez les migrations :
  

  
python manage.py makemigrations
python manage.py migrate
Créez un superutilisateur :
  

  
python manage.py createsuperuser
Lancez le serveur :
  

  
python manage.py runserver
Structure du Projet
plaintext

  
blog_project/
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
Accédez à /admin pour gérer les articles et catégories.
Créez des catégories avant de créer des articles.
Gestion des Articles
Liste des articles : /
Création d'article : /post/new/
Détail d'un article : /post/<id>/
Modification : /post/<id>/edit/
Suppression : /post/<id>/delete/
Logs
Les logs sont configurés pour enregistrer :

Les accès aux articles
Les créations/modifications/suppressions
Les tentatives d'accès non autorisées
Contribution
Fork le projet.
Créez une branche :
  

  
git checkout -b feature/AmazingFeature
Committez vos changements :
  

  
git commit -m 'Add some AmazingFeature'
Push vers la branche :
  

  
git push origin feature/AmazingFeature
Ouvrez une Pull Request.
License
Ce projet est sous licence MIT.

Contact
Pour toute question, vous pouvez me contacter à : mohamed.djabi@outlook.fr


  

### Notes

- N'hésitez pas à personnaliser le contenu selon vos besoins.
- Assurez-vous que les liens et les informations sont à jour et corrects.