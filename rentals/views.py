from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Rental
from .serializers import RentalSerializer
from spots.models import Spot

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all().select_related('spot','tenant')
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # tenants see their rentals; landlords see rentals of their spots
        if user.user_type == 'tenant':
            return Rental.objects.filter(tenant=user)
        return Rental.objects.filter(spot__owner=user)

    def perform_create(self, serializer):
        spot = serializer.validated_data['spot']
        serializer.save(tenant=self.request.user, monthly_price=spot.price)

    @action(detail=False, methods=['get'], url_path='my-rentals')
    def my_rentals(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='owner-history')
    def owner_history(self, request):
        user = request.user
        # only landlords should access owner history
        if getattr(user, 'user_type', None) != 'landlord':
            return Response({'detail': 'Apenas proprietários podem acessar este recurso.'}, status=status.HTTP_403_FORBIDDEN)

        qs = Rental.objects.filter(spot__owner=user).select_related('spot', 'tenant')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
