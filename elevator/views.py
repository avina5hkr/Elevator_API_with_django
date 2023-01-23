from rest_framework import viewsets
from rest_framework.mixins import UpdateModelMixin
from elevator import models, serializers



class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = models.Elevator.objects.all()
    serializer_class = serializers.ElevatorSerializer



