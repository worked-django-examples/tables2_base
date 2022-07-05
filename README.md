[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/worked-django-examples/tables2_base)

# Demos, walkthrus, code inspection django-tables2

from https://github.com/worked-django-examples 

## Purpose

This is a base for creating examples of django-tables2 examples on gitpod.
The gitpod image will load django and postgres, and a couple tables with
country population data.

### repo setup 

 - `pip install django_tables2 tablib bootstrap4 psycopg2-binary python-env`**** 
    (or `pip install -r requirementsl.txt`)
 - `django-admin startproject config`
 - `mv config django`
 - create `.gitignore`
 - add `.env` to `.gitignore`
 - change settings for passwords/CSRF secrets
 - add files from worldbank to "etl/worldbank"
 ## 

## to run on your local with docker

`docker run --name postgresql -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 --restart always -v /tmp/pgdata:/tmp/var/lib/postgresql/data -d postgres:13`

run the worldbank-population.py script in the etl directory
