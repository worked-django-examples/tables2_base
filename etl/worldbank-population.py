import csv
import os

import psycopg2 as pg
import configparser

DATAFILE = "./worldbank/Data.csv"

DEFAULT_CONFIG_FILE = "./etl_config.ini"
GITPOD_CONFIG_FILE = "./etl_config_gitpod.ini"

if os.getenv("GITPOD_WORKSPACE_CONTEXT", False):
    config_file = GITPOD_CONFIG_FILE
else:
    config_file = DEFAULT_CONFIG_FILE

# Series Name,"Series Code","Country Name","Country Code","2000 [YR2000]","2001 [YR2001]","2002 [YR2002]","2003 [YR2003]","2004 [YR2004]","2005 [YR2005]","2006 [YR2006]","2007 [YR2007]","2008 [YR2008]","2009 [YR2009]","2010 [YR2010]","2011 [YR2011]","2012 [YR2012]","2013 [YR2013]","2014 [YR2014]","2015 [YR2015]"

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

inserts = []
with open(DATAFILE, "rt", encoding="utf-8-sig") as data:
    reader = csv.DictReader(data, quotechar='"')
    for i, row in enumerate(reader):
        if row["Series Name"] == "Population, total":
            country = row['Country Code']
            for year_column in YEAR_COLUMNS:
                try:
                    population = int(row[year_column])
                except Exception  as e:
                    print(f"no population for {country} for {year_column}")
                    print(e)
                    population = None
                year = int(year_column[:4])
                inserts.append({"country": country,
                                "year": year,
                                "population": population})
                                
    print(f"Length of inserts: {len(inserts)}")
    
                                
