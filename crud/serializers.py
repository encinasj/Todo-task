from rest_framework import serializers
from crud.models import Crud

class CrudSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crud
        fields = ('id', 'title', 'description', 'completed')

