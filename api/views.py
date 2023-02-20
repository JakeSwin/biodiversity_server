from django.shortcuts import render


# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.
# Will output all users
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    

