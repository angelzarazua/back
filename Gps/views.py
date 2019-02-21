from rest_framework import generics
from .models import Gps
from .serializers import GpsSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class Gps(generics.ListCreateAPIView):
    queryset = Gps.objects.all()
    serializer_class = GpsSerializer

    def getObject(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs[''],
        )

        return obj
