from rest_framework import serializers

from .models import Rental
from spots.serializers import SpotSerializer
from spots.models import Spot


class RentalSerializer(serializers.ModelSerializer):
    spot = SpotSerializer(read_only=True)
    spot_id = serializers.PrimaryKeyRelatedField(queryset=Spot.objects.all(), write_only=True, source='spot')
    monthly_price = serializers.FloatField(read_only=True)
    tenant_name = serializers.CharField(source='tenant.name', read_only=True)

    class Meta:
        model = Rental
        fields = ['id','spot','spot_id','tenant','tenant_name','start_date','end_date','status','monthly_price']
        read_only_fields = ['tenant','tenant_name']

    def create(self, validated_data):
        return super().create(validated_data)
