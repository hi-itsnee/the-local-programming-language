# Filename:                haversine.py
# Author:                  Team 13
# Description:             local language conversion module
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-29 23:26:02 plt>

def convertdist(a, b, c="m"):
    if (c == "ft"):
        if (b == "m"):
            a = a / 3.281
        elif (b == "mi"):
            a = a / 5280.00
    elif (c == "mi"):
        if (b == "m"):
            a = a * 1609.3
        elif ( b == "ft"):
            a = a * 5280.0
    elif (c == "m"):
        if ( b == "mi"):
            a = a / 1609.3
        elif (b == "ft"):
            a = a * 3.281
    return a
