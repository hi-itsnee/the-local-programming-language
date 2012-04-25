# Filename:                coord_fn.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 10:53:41 plt>

#import math
from localast import Node
# Node(type, children=None, value=None, line=None)

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
    p[0] = Node("Dist", None,"haversine.haversine(%s,%s)"%(p[3],p[5]))

def p_dist_coord(p):
    '''dist_coord : DIST LPAREN COORD COMMA COORD RPAREN'''
    p[0] = Node("Dist", None,"haversine.haversine(\"%s\",\"%s\")"%(p[3],p[5]))

def p_convertdist(p):
    '''convertdist : CONVERTDIST'''
