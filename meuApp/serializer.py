from rest_framework import serializers
from .models import CDB

class CDBSerializer(serializers.ModelSerializer):

    class Meta:

        model = CDB
        fields = '__all__'