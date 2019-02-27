''' author:  @MOhit: devmohit-live
A gps route tracking system'''

import csv
from gmplot import gmplot as gmp
# print('Working')
gmap=gmp.GoogleMapPlotter(28.689169,77.324448,17)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s"

with open('route.csv','r') as f:
    reader=csv.reader(f)
    k=0

    for row in reader:
        lat=float(row[0])
        lng=float(row[1])

        if(k==0):
            gmap.marker(lat,lng,'blue')
            k=1
        else:
            gmap.marker(lat,lng,'green')

        
gmap.marker(lat,lng,'red')
gmap.draw('mymap.html')