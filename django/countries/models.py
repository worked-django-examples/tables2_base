from django.db import models
from django.db.models.constraints import UniqueConstraint

# Create your models here.


class Country(models.Model):
    country_code = models.CharField(max_length=5, primary_key=True)
    name = models.TextField(null=False)


class AnnualPopulation(models.Model):

    country = models.ForeignKey(Country, on_delete=models.CASCADE, name="country")
    year = models.IntegerField(null=False)
    population = models.IntegerField(null=True)
    year_country = models.CharField(max_length=9, unique=True)
    # year_country is for uniqueness since foreign
    # key can't be part of composite unique

    
