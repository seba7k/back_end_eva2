"""
Archivo de configuración principal del proyecto Django.
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-....' # Tu secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps de terceros
    'rest_framework',
    'django_filters',
    'drf_yasg', # Para la documentación de la API

    # Mi app
    'gestion_medica',
]

MIDDLEWARE = [
    # ... (contenido original)
]

ROOT_URLCONF = 'clinica_vital.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Permite tener una carpeta de templates general
        'APP_DIRS': True,
        'OPTIONS': {
            # ... (contenido original)
        },
    },
]

WSGI_APPLICATION = 'clinica_vital.wsgi.application'

# Database
# Configuración para PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eva2_db',       # Nombre de tu BD
        'USER': 'postgres',     # Tu usuario de PostgreSQL
        'PASSWORD': 'tu_password', # Tu contraseña
        'HOST': 'localhost',      # O la IP del servidor de BD
        'PORT': '5432',
    }
}

# ... (resto del archivo)