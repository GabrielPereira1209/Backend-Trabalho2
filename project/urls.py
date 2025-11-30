
# importa módulos necessários para urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# configura a documentação swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Parking API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# define as rotas principais do projeto
urlpatterns = [
    path('admin/', admin.site.urls), # rota do admin
    path('api/', include('users.urls')), # rotas dos usuários
    path('api/', include('spots.urls')), # rotas das vagas
    path('api/', include('rentals.urls')), # rotas das reservas
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # rota da documentação swagger
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # rota da documentação redoc
]
