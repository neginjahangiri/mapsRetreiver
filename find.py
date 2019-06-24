import os
import requests
import urllib
import shutil
import csv

citiesCount = 300
citiesData = []
with open("chosenCities.csv","r") as f:
    data = csv.reader(f,dialect='excel')
    next(data)
    for row in data:
        citiesData.append(row)
i = 0
for row in citiesData[:citiesCount]:
    city_name, country_name = (row[0],row[1])
    i=i+1
    if city_name=='Long Beach':
        print(str(i))
