from django.contrib import admin
from django.urls import path
from .views import UserView, UserPost

urlpatterns = [
    path('get/', UserView.as_view()),
    path('post/', UserPost.UserPost()),
]