from django.db import models

class Bankwell(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    regestered_name = models.CharField(max_length=255)
    anury_capicity = models.IntegerField()

    def __str__(self):
        return self.firstname


