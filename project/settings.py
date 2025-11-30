# importa módulos necessários
import os
from datetime import timedelta
from pathlib import Path

# define o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# chave secreta do django
SECRET_KEY = os.environ.get('DJANGO_SECRET', 'dev-secret')

# ativa ou desativa o modo debug
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'

# hosts permitidos para acesso
ALLOWED_HOSTS = ['*']

 # apps instalados no projeto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'drf_yasg',
    'users',
    'spots',
    'rentals',
]

 # middlewares utilizados
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# arquivo de urls principal
ROOT_URLCONF = 'project.urls'

 # configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# aplicação wsgi
WSGI_APPLICATION = 'project.wsgi.application'

 # configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# validadores de senha
AUTH_PASSWORD_VALIDATORS = []

# configurações de internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# url dos arquivos estáticos
STATIC_URL = '/static/'

# campo padrão para chaves primárias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# modelo de usuário customizado
AUTH_USER_MODEL = 'users.User'

 # configuração do rest framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

 # configuração do simple jwt
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
}

# permite requisições de qualquer origem
CORS_ALLOW_ALL_ORIGINS = True
