from django.db import models

## Create a database model that can be used to store the point coordinates and the plant species at that point 
class plantPoint(models.Model):
    # Primary key built into django
    
    # Used to identify the plant
    plantName = models.CharField(max_length=60)
    
    # Coordinates of the point
    latCoord = models.FloatField(max_length=10)
    longCoord = models.FloatField(max_length=10)
    
    # When printing out this class print out its plantName
    def __str__(self):
        return f'{self.plantName} ({self.latCoord}, {self.longCoord})'