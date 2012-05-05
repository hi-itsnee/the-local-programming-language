# Filename:                haversine.py
# Author:                  Team 13
# Description:             local language Haversine module
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-05 17:44:24 plt>

import math

def dist(c1, c2):
    lat1, lon1 = map(lambda x: float(x), c1.strip()[1:-1].split(","))
    lat2, lon2 = map(lambda x: float(x), c2.strip()[1:-1].split(","))
    alat = math.radians(lat1)
    alon = math.radians(lon1)
    blat = math.radians(lat2)
    blon = math.radians(lon2)
    hlat = alat - blat
    hlon = alon - blon
    hlat = (1 - math.cos(hlat)) / 2
    hlon = (1 - math.cos(hlon)) / 2
    foo = math.cos(alat) * math.cos(blat) * hlon
    foo = foo + hlat
    radius = 6371
    d = 2 * radius * math.asin(math.sqrt(foo))
    return d
