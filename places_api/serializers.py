from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'locationName', 'locationAddress', 'locationCity', 'locationState', 'tableSize', 'tableBrand', 'tableCondition', 'cueCondition', 'vibe', 'newFriends')
