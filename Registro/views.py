from rest_framework import generics
from .models import Registro
from .serializers import RegistroSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class Registro(generics.ListCreateAPIView):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

    def getObject(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs[''],
        )

        return obj