import csv
import os
from collections import defaultdict
from psycopg2.extras import execute_batch

import psycopg2 as pg
import configparser

DATAFILE = "./worldbank/Data.csv"

DEFAULT_CONFIG_FILE = "./etl_config.ini"
GITPOD_CONFIG_FILE = "./etl_config_gitpod.ini"

if os.getenv("GITPOD_WORKSPACE_CONTEXT", False):
    config_file = GITPOD_CONFIG_FILE
else:
    config_file = DEFAULT_CONFIG_FILE

configp = configparser.ConfigParser()
configp.read(config_file)
postgres = configp["postgres"]
port, password, user, database, host = (
    postgres["port"],
    postgres["password"],
    postgres["user"],
    postgres["database"],
    postgres["url"],
)


# connect to the database before bothering to read the data
dbconn = pg.connect(dbname=database, user=user, password=password, host=host, port=port)
dbcursor = dbconn.cursor()


# Series Name',"Series Code","Country Name","Country Code","2000 [YR2000]","2001 [YR2001]","2002 [YR2002]","2003 [YR2003]","2004 [YR2004]","2005 [YR2005]","2006 [YR2006]","2007 [YR2007]","2008 [YR2008]","2009 [YR2009]","2010 [YR2010]","2011 [YR2011]","2012 [YR2012]","2013 [YR2013]","2014 [YR2014]","2015 [YR2015]"

YEAR_COLUMNS = [
    "2000 [YR2000]",
    "2001 [YR2001]",
    "2002 [YR2002]",
    "2003 [YR2003]",
    "2004 [YR2004]",
    "2005 [YR2005]",
    "2006 [YR2006]",
    "2007 [YR2007]",
    "2008 [YR2008]",
    "2009 [YR2009]",
    "2010 [YR2010]",
    "2011 [YR2011]",
    "2012 [YR2012]",
    "2013 [YR2013]",
    "2014 [YR2014]",
    "2015 [YR2015]",
]

population_inserts = []

country_inserts = []

with open(DATAFILE, "rt", encoding="utf-8-sig") as data:
    reader = csv.DictReader(data, quotechar='"')
    for i, row in enumerate(reader):
        if row["Series Name"] == "Population, total":
            country = row["Country Code"]
            country_inserts.append(
                {"country_code": country, "name": row["Country Name"]}
            )
            for year_column in YEAR_COLUMNS:
                try:
                    population = int(row[year_column])
                except Exception as e:
                    print(f"no population for {country} for {year_column}")
                    print(e)
                    population = None
                year = int(year_column[:4])
                population_inserts.append(
                    {
                        "year": year,
                        "population": population,
                        "country_id": country,
                        "year_country": f"{year}{country}",
                    }
                )

    COUNTRY_SQL = """insert into countries_country
                  VALUES
                  (%(country_code)s, %(name)s)
                  ON CONFLICT(country_code) DO NOTHING"""
    execute_batch(dbcursor, sql=COUNTRY_SQL, argslist=country_inserts)
    dbconn.commit()

    dbcursor = dbconn.cursor()

    ANNUAL_POP_SQL = """insert into countries_annualpopulation\
            (country_id, year, population, year_country)
            VALUES
            (%(country_id)s,  %(year)s, %(population)s, %(year_country)s)
            ON CONFLICT(year_country) DO UPDATE
            SET population = %(population)s
"""
    execute_batch(dbcursor, sql=ANNUAL_POP_SQL, argslist=population_inserts)

    dbconn.commit()

    print("done")
