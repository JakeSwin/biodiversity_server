from django.contrib import admin

# Add models here to add them to admin panel
from .models import plantPoint


admin.site.register(plantPoint)