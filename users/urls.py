# urls do app users
from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.register),
    path('auth/login/', views.login),
    path('auth/me/', views.me),
    path('auth/profile/', views.update_profile),
    path('auth/change-password/', views.change_password),
    path('auth/forgot-password/', views.forgot_password),
]
