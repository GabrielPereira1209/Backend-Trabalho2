from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpotViewSet

router = DefaultRouter()
router.register('spots', SpotViewSet, basename='spot')

urlpatterns = [
    path('', include(router.urls)),
]
