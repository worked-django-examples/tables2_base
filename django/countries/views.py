from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import AnnualPopulation


def index(request):
    db_hello_world_qset = AnnualPopulation.objects.filter(country__name__contains="ico")

    def facts(i):
        something = db_hello_world_qset[i]
        year = something.year
        country = something.country.name
        population = something.population
        return(year, country, population)

    the_facts = ""
    for offset in [5, 25, 15]:
        year, country, population = facts(offset)
        the_facts = (f"{the_facts}<P>"
                     f"the population {country} was {population} "
                     f"in {year}")

    return HttpResponse(
        ("wireframe -- this is countries.views.index"
         "<P>some data:</P>"
         f"{the_facts}"))
