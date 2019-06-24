import os
import requests
import urllib
import shutil
import csv

citiesCount = 400
citiesFileName="chosenCities2.csv"
def applyParameters(url,parameters):
    #add the parameters to the url
    resultURL = url
    for i in range(len(parameters)):
        resultURL += parameters[i][0] + \
             '=' + parameters[i][1]
        if i != len(parameters) - 1:
            resultURL += '&'
    return resultURL

with open ("apiKey.txt","r") as apiKeyFile:
    apiKey = apiKeyFile.readline()

citiesData = []
with open(citiesFileName,"r") as f:
    data = csv.reader(f,dialect='excel')
    next(data)
    for row in data:
        citiesData.append(row)


# Google's base API url
url = \
    'https://maps.googleapis.com/maps/api/staticmap?' 
# Detailed information on the use of parameters at:
# https://developers.google.com/maps/documentation/maps-static/dev-guide#MapTypes

parameters =[
    ['key',apiKey],
# the image size (in pixels)
    ['size','700x700'],
# the image format
    ['format','png'],
    ['output','classic'],
# Zoom appriximation
#    1: World
#    5: Landmass/continent
#    10: City
#    15: Streets
#    20: Buildings
    ['zoom','18'],
    ['scale','2'],
# remove the labels (i.e. road and city names)
# more styling options : https://mapstyle.withgoogle.com/],
]


for row in citiesData[:citiesCount]:
    #terrain
    thisCityParameters = parameters.copy()
    city_name, country_name = (row[0],row[1])
    thisCityParameters.append(['center',city_name + ','+country_name])
    # the type of the map,
    # options available [roadmap, satellite, terrain, hybrid]
    thisCityParameters.append(['maptype','roadmap'])
    thisCityParameters.append(['style','element:geometry%7Ccolor:0xebe3cd'])
    thisCityParameters.append(['style','element:labels%7Cvisibility:off'])
    thisCityParameters.append(['style','element:labels.text.fill%7Ccolor:0x523735'])
    thisCityParameters.append(['style','element:labels.text.stroke%7Ccolor:0xf5f1e6'])
    thisCityParameters.append(['style','feature:administrative%7Celement:geometry.stroke%7Ccolor:0xc9b2a6'])
    thisCityParameters.append(['style','feature:administrative.land_parcel%7Cvisibility:off'])
    thisCityParameters.append(['style','feature:administrative.land_parcel%7Celement:geometry.stroke%7Ccolor:0xdcd2be'])
    thisCityParameters.append(['style','feature:administrative.land_parcel%7Celement:labels.text.fill%7Ccolor:0xae9e90'])
    thisCityParameters.append(['style','feature:administrative.neighborhood%7Cvisibility:off'])
    thisCityParameters.append(['style','feature:landscape.man_made%7Celement:geometry.fill%7Ccolor:0xaf6d32'])
    thisCityParameters.append(['style','feature:landscape.man_made%7Celement:geometry.stroke%7Ccolor:0x000000%7Cweight:2'])
    thisCityParameters.append(['style','feature:landscape.natural%7Celement:geometry%7Ccolor:0xdfd2ae'])
    thisCityParameters.append(['style','feature:poi%7Celement:geometry%7Ccolor:0xdfd2ae'])
    thisCityParameters.append(['style','feature:poi%7Celement:labels.text.fill%7Ccolor:0x93817c'])
    thisCityParameters.append(['style','feature:poi.park%7Celement:geometry.fill%7Ccolor:0xa5b076'])
    thisCityParameters.append(['style','feature:poi.park%7Celement:geometry.stroke%7Cweight:2'])
    thisCityParameters.append(['style','feature:poi.park%7Celement:labels.text.fill%7Ccolor:0x447530'])
    thisCityParameters.append(['style','feature:road%7Celement:geometry%7Ccolor:0xf5f1e6'])
    thisCityParameters.append(['style','feature:road%7Celement:geometry.fill%7Ccolor:0xffffff'])
    thisCityParameters.append(['style','feature:road.arterial%7Celement:geometry%7Ccolor:0xfdfcf8'])
    thisCityParameters.append(['style','feature:road.highway%7Celement:geometry%7Ccolor:0xf8c967'])
    thisCityParameters.append(['style','feature:road.highway%7Celement:geometry.fill%7Ccolor:0xffffff'])
    thisCityParameters.append(['style','feature:road.highway%7Celement:geometry.stroke%7Ccolor:0xe9bc62'])
    thisCityParameters.append(['style','feature:road.highway.controlled_access%7Celement:geometry%7Ccolor:0xe98d58'])
    thisCityParameters.append(['style','feature:road.highway.controlled_access%7Celement:geometry.stroke%7Ccolor:0xdb8555'])
    thisCityParameters.append(['style','feature:road.local%7Celement:labels.text.fill%7Ccolor:0x806b63'])
    urlToSend=applyParameters(url,thisCityParameters)

    r = requests.get(urlToSend, timeout=20)
    if r.status_code == 200:
        with open(os.path.join(os.getcwd(),'data','b',city_name+','+country_name+".png"), "wb") as f:
            f.write(r.content)
            print("[plan] picture saved :"+city_name+','+country_name)
    else:
        print("Error while getting the picture;URL = "+url)

    thisCityParameters = parameters.copy()
    thisCityParameters.append(['center',city_name + ','+country_name])
    thisCityParameters.append(['maptype','satellite'])
    urlToSend=applyParameters(url,thisCityParameters)
    print("[satellite] sending the request :"+city_name+','+country_name)
    
    r = requests.get(urlToSend, timeout=20)
    
    if r.status_code == 200:
        with open(os.path.join(os.getcwd(),'data','a',city_name+','+country_name+".png"), "wb") as f:
            f.write(r.content)
            print("[areal] picture saved :"+city_name+','+country_name)
    else:
        print("Error while getting the picture;URL = "+url)
