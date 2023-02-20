from django.shortcuts import render

# New tutorial
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.
# Will output all users
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# @api_view(['POST'])
# def UserPost(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
    

