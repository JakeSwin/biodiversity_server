from django.shortcuts import render
from rest_framework import viewsets


# Create the APIs here
from .models import plantPoint
from .serializers import plantPointSer


# Return all plants in database
class plantViewSet(viewsets.ModelViewSet):
    queryset = plantPoint.objects.all().order_by('plantName')
    serializer_class = plantPointSer
# ModelViewSet - sets up post and get for us
# Need to look into getting this data using JS






# Search for plant by plantName and return all