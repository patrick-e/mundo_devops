from rest_framework import viewsets
from api.api import serializers
from api.models import Data

class DataViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DataSerializer
    queryset = Data.objects.all()
    