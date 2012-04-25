# Filename:                coord_fn.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 10:53:41 plt>

#import math
from localast import Node
# Node(type, children=None, value=None, line=None)
import re

def p_coord_fn(p):
    '''coord_fn : dist
                | convertdist'''
    p[0] = Node("Coord_fn", [p[1]])

def p_dist(p):
    '''dist : dist_id
            | dist_coord'''
    p[0] = Node("Dist",[p[1]])

def p_dist_id(p):
    '''dist_id : DIST LPAREN ID COMMA ID RPAREN'''
    value = "0"
    value = value + "\nalat = math.radians(%s[0])" % (p[3])
    value = value + "\nalon = math.radians(%s[1])" % (p[3])
    value = value + "\nblat = math.radians(%s[0])" % (p[5])
    value = value + "\nblon = math.radians(%s[1])" % (p[5])
    value = value + "\nhlat = alat - blat"
    value = value + "\nhlon = alon - blon"
    value = value + "\nhlat = (1-math.cos(hlat)) / 2"
    value = value + "\nhlon = (1-math.cos(hlon)) / 2"
    value = value + "\nfoo = math.cos(alat) * math.cos(blat) * hlon"
    value = value + "\nfoo = foo + hlat"
    value = value + "\nradius = 6371"
    value = value + "\nd = 2 * radius * math.asin(math.sqrt(foo))"
    value = value + "\nreturn d"
    p[0] = Node("Dist", None,value)

def p_dist_coord(p):
    '''dist_coord : DIST LPAREN COORD COMMA COORD RPAREN'''
    value = "0"
    mo = re.search('(?P<lat>[+-]?\d+\.\d+)\s*,\s*(?P<longi>[+-]?\d+\.\d+)', p[3])
    value = value + "\nalat = math.radians(%f)" % (float(mo.group('lat')),)
    value = value + "\nalon = math.radians(%f)" % (float(mo.group('longi')),)
    mo = re.search('(?P<lat>[+-]?\d+\.\d+)\s*,\s*(?P<longi>[+-]?\d+\.\d+)', p[5])
    value = value + "\nblat = math.radians(%f)" % (float(mo.group('lat')),) 
    value = value + "\nblon = math.radians(%f)" % (float(mo.group('longi')),)
    value = value + "\nhlat = alat - blat"
    value = value + "\nhlon = alon - blon"
    value = value + "\nhlat = (1-math.cos(hlat)) / 2"
    value = value + "\nhlon = (1-math.cos(hlon)) / 2"
    value = value + "\nfoo = math.cos(alat) * math.cos(blat) * hlon"
    value = value + "\nfoo = foo + hlat"
    value = value + "\nradius = 6371"
    value = value + "\nd = 2 * radius * math.asin(math.sqrt(foo))"
    value = value + "\nreturn d"
    p[0] = Node("Dist", None,value)


def p_convertdist(p):
    '''convertdist : CONVERTDIST'''
