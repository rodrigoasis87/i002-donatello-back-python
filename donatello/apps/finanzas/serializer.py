from rest_framework import serializers
from .models import Finanza

class FinanzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finanza
        fields = ('id_finanza', 'tipo', 'monto', 'fecha', 'id_usuario')
