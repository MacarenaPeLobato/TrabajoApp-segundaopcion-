from django.db import models

# Create your models here.

class Familia (models.Model):
    nombrepadre= models.CharField(max_length=15)
    nombremadre= models.CharField(max_length=15)
    nombrehijo= models.CharField(max_length=15)
    nombrehija= models.CharField(max_length=15)
    dnipadre= models.IntegerField()
    dnimadre= models.IntegerField()
    cumplehijo= models.CharField(max_length=15)
    cumplehija= models.CharField(max_length=15)

    
    