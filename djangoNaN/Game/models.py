from django.db import models

# Create your models here.


class Equipe(models.Model):
    name = models.CharField(max_length=50,blank=True)
    cote = models.CharField(max_length=10)
    description = models.CharField(max_length=150)


    def __str__(self):
        return self.name



class Paris(models.Model):
    name = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    montant_paris = models.IntegerField()
    equipe = models.CharField( max_length=50)

    def __str__(self):
        return self.name
