from rest_framework import serializers
from .models import Banks,Branches    

class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'