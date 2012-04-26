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
    '''dist : DIST LPAREN atom COMMA atom RPAREN'''
    p[0] = Node("dist", [p[3],p[5]], None, "haversine.fish(%s,%s)")

def p_convertdist(p):
    '''convertdist : CONVERTDIST LPAREN atom COMMA atom COMMA atom RPAREN
                   | CONVERTDIST LPAREN atom COMMA atom RPAREN'''
    if len(p) == 9:
        p[0] = Node("convertdist", [p[3],p[5],p[7]], None, "conversion.fly(%s,\"%s\",\"%s\")")
    else:
        p[0] = Node("convertdist", [p[3],p[5]], None, "conversion.fly(%s,\"%s\")")

