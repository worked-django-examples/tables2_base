[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/worked-django-examples/tables2_base)

# Demos, walkthrus, code inspection django-tables2

# from github.com/worked-django-examples 

## Purpose

This is a base for creating examples of django-tables2 examples on gitpod.
The gitpod image will load django and postgres.

## setup 

 - `pip install django_tables2 tablib bootstrap4 psycopg2-binary python-env`**** 
    (or `pip install -r requirementsl.txt`)
 - `django-admin startproject config`
 - `mv config django`
 - create `.gitignore`
 - add `.env` to `.gitignore`
 - change settings for passwords/CSRF secrets
 ## 

## to run on your local with docker

`docker run --name postgresql -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 --restart always -v /tmp/pgdata:/tmp/var/lib/postgresql/data -d postgres:13`