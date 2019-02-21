from rest_framework import generics
from .models import Unidades
from .serializers import UnidadesSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class Unidades(generics.ListCreateAPIView):
    queryset = Unidades.objects.all()
    serializer_class = UnidadesSerializer

    def getObject(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs[''],
        )

        return obj