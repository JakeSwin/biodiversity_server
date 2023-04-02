from rest_framework import serializers

# Add models to serialise (turn to JSON)
from .models import plantPoint

class plantPointSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = plantPoint
        fields = ('plantName', 'latCoord', 'longCoord')
    