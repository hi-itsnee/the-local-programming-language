# Filename:                haversine.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 10:53:41 plt>

import math
import sys
# Node(type, children=None, value=None, line=None)

def fish(a,b):
    alat = math.radians(a[0])
    alon = math.radians(a[1])
    blat = math.radians(b[0])
    blon = math.radians(b[1])
    hlat = alat - blat
    hlon = alon - blon
    hlat = (1-math.cos(hlat)) / 2
    hlon = (1-math.cos(hlon)) / 2
    foo = math.cos(alat) * math.cos(blat) * hlon
    foo = foo + hlat
    radius = 6371
    d = 2 * radius * math.asin(math.sqrt(foo))
    return d
