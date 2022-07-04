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
        the_facts = (
            f"{the_facts}<P>"
            f"the population of {country} was {population} "
            f"in {year}"
        )

    so_what = """<P><b>If you are looking at this gitpod</b>, and see
                 population numbers about countries above, it means Django is running
                 and pulling data from a postrgres database.  

                 <P>you can start a new shell and run <code>python manage.py shell</code> or other django stuff like
                 <code>startapp</app>.

                 <P>Look at <code>.gitpod.yml</code> and  <code>.gitpod.Dockerfile</code> to see the gitpod-specific 
                 parts for running postgres & staging data.
                 <P>------------- end of countries.views.index"""
    return HttpResponse(
        (
            "wireframe -- this is countries.views.index"
            "<P>some data:</P>"
            f"{the_facts}"
            f"{so_what}"
        )
    )

