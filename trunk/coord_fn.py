# Filename:                coord_fn.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 10:53:41 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_coord_fn(p):
    '''coord_fn : dist
                | convertdist'''

def p_dist(p):
    '''dist : DIST'''

def p_convertdist(p):
    '''convertdist : CONVERTDIST'''
