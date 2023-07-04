from django.shortcuts import render
from django.http import HttpResponse
import joblib
from math import radians,tan
from pyproj import Proj
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.path as mpath
import networkx as nx
# Create your views here.
def pathplanning(request):
    import json
    if request.method=='POST':
        cordinates = request.POST
        cordinates1 = dict(cordinates)
        print(cordinates1)
        cr=[]
        for key,value in cordinates1.items():
            if key.startswith('cordinates'):
                cr.append(value)
        cor = []
        for i in cr:
            lat = float(i[0])
            lan = float(i[1])
            d = [lat,lan]
            cor.append(d)
        # print(cor)
        final_path_with_lat_lng = "done"
    # print(final_path_with_lat_lng)
    import json
    path_geojson = {
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": final_path_with_lat_lng
    },
    "properties": {}
}
    path_geojson_str = json.dumps(path_geojson)
    return HttpResponse(path_geojson_str)
