from rest_framework import serializers
from .models import *


class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Crud
        fields = '__all__'

