# Filename:                coord_fn.py
# Author:                  Team 13
# Description:             local language parser coordinate functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-29 23:23:29 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_coord_fn(p):
    '''coord_fn : dist
                | convertdist'''
    p[0] = Node("coord_fn", [p[1]])

def p_dist(p):
    '''dist : DIST LPAREN atom COMMA atom RPAREN'''
    p[0] = Node("dist", [p[3], p[5]], None, "dist(%s, %s)")

def p_convertdist(p):
    '''convertdist : CONVERTDIST LPAREN atom COMMA atom COMMA atom RPAREN
                   | CONVERTDIST LPAREN atom COMMA atom RPAREN'''
    if len(p) == 9:
        p[0] = Node("convertdist", [p[3], p[5], p[7]], None,
                    "convertdist(%s, %s, %s)")
    elif len(p) == 7:
        p[0] = Node("convertdist", [p[3], p[5]], None,
                    "convertdist(%s, %s)")
