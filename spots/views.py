# importa módulos necessários para views
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Spot
from .serializers import SpotSerializer

 # permissão para permitir apenas o dono editar
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

 # viewset para operações de vaga
class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all().select_related('owner')
    serializer_class = SpotSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # define o usuário como dono ao criar vaga
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # retorna queryset filtrado por parâmetros de busca
    def get_queryset(self):
        qs = super().get_queryset()
        location = self.request.query_params.get('location')
        type_ = self.request.query_params.get('type')
        max_price = self.request.query_params.get('max_price')
        if location:
            qs = qs.filter(location__icontains=location)
        if type_:
            qs = qs.filter(type=type_)
        if max_price:
            try:
                mp = float(max_price)
                qs = qs.filter(price__lte=mp)
            except ValueError:
                pass
        return qs

    # endpoint para listar vagas do usuário
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated], url_path='my-spots')
    def my_spots(self, request):
        qs = Spot.objects.filter(owner=request.user)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
