from django.db import models

# Create your models here.
# Create users and a group number they are in
class User(models.Model):
    username = models.CharField(max_length=20, null=False, unique=True)
    groupID = models.PositiveSmallIntegerField(null=False, unique=False)