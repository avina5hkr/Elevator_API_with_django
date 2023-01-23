from rest_framework import viewsets
from rest_framework.mixins import UpdateModelMixin
from elevator import models, serializers
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from elevator import utils


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = models.Elevator.objects.all()
    serializer_class = serializers.ElevatorSerializer


