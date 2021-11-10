from django.db import models

# Create your models here.
class Footfall(models.Model):
    time = models.DateTimeField()
    footsteps = models.IntegerField()

    def __str__(self):
        return f"Time: {self.time} Steps: {self.footsteps}"