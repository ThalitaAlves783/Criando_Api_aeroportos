from rest_framework import  serializers
from aeroporto.models import Aeroporto

class AeroportoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeroporto
        fields = '__all__'