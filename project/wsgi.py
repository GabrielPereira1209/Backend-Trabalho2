# importa os módulos necessários
import os
from django.core.wsgi import get_wsgi_application

# define o módulo de configurações do django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# cria a aplicação wsgi
application = get_wsgi_application()
