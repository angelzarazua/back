from rest_framework import serializers
from .models import Gps

class GpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gps
        fields = ('__all__')