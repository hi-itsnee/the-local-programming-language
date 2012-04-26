# Filename:                haversine.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 10:53:41 plt>

import math
import sys
# Node(type, children=None, value=None, line=None)

def fly(a, b, c = "m"):
    if (c == "ft"):
        if ( b == "m"):
            a =  a / 3.281
        elif (b == "mi"):
            a = a / 5280.00
    elif (c == "mi"):
        if ( b == "m"):
            a = a * 1609.3
        elif ( b == "ft"):
            a = a * 5280
    elif (c == "m"):
        if ( b == "mi"):
            a = a / 1609.3
        elif ( b == "ft"):
            a = a * 3.281
    return a
