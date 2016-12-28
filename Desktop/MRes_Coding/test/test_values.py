
import numpy as np
import geopy
from io import BytesIO
from matplotlib import image as img
import requests
from graph import Greengraph

def test_values():
    geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
    latlong = geocoder.geocode('Chicago', exactly_one=False)[0][1]

    print(latlong[0])
    print(latlong[1])
    
    lat=latlong[0]
    long=latlong[1]
    
    satellite=True
    zoom=10
    size=(400,400)
    sensor=False

    base="http://maps.googleapis.com/maps/api/staticmap?"
    params=dict(
        sensor= str(sensor).lower(),
        zoom= zoom,
        size= "x".join(map(str, size)),
        center= ",".join(map(str, (lat, long) )),
        style="feature:all|element:labels|visibility:off"
     )
            
    if satellite: params["maptype"]="satellite"
    


    image = requests.get(base, params=params).content

test_values()

lls=Greengraph.location_sequence(Greengraph("",""), (40.7127,-74.0059),(41.8781, -87.6297),20)
print(lls)[0])
print(lls[1])

[ 40.7127 -74.0059]
[ 40.77403684 -74.72294211]








