from django.db import models

# Create your models here.
class categorie(models.Model):
    name=models.CharField(max_length=200)
    date_add=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-date_add']


class produit(models.Model):
    titre=models.CharField(max_length=200)
    prix=models.FloatField(default=0.00)
    stock=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    img=models.ImageField(upload_to="products",blank=True,null=True)
    

