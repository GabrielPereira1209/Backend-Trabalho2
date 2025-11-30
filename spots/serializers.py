# importa módulos necessários para serializers
from rest_framework import serializers
from .models import Spot
from users.serializers import UserSerializer

 # serializer para vaga
class SpotSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.name', read_only=True)
    price = serializers.FloatField()

    class Meta:
        model = Spot
        fields = ['id','title','description','location','type','price','available','owner','owner_name']
        read_only_fields = ['owner','owner_name']
