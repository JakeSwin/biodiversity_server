from django.apps import AppConfig
from django.contrib import admin
from .models import User


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

admin.site.register(User)