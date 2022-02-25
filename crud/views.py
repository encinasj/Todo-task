from pkgutil import ImpImporter
from pyclbr import Class
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CrudSerializer
from .models import Crud


class CrudView(viewsets.ModelViewSet):
    serializer_class = CrudSerializer
    queryset = Crud.objects.all()
