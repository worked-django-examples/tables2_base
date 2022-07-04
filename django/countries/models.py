from django.db import models

# Create your models here.

class Country(models.Model):
    country_code = models.CharField(max_length=5, primary_key=True)
    name = models.TextField(null=False) 
class AnnualPopulation(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    population = models.IntegerField(null=True)
