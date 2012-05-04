# Filename:              atom.py
# Author:                Team 13
# Description:           local parser atoms
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-05-04 15:25:50 plt>

from localast import Node

def p_atom(p):
    '''atom : ID
            | NUMBER
            | BOOL
            | NULL
            | COORD
            | STRING
            | LIST
            | ID LT NUMBER GT
            | COORD LT NUMBER GT
            | LIST LT NUMBER GT
            | ID LT ID GT
            | COORD LT ID GT
            | LIST LT ID GT'''
    if len(p) == 2:
        p[0] = Node("atom", None, p[1])
    elif len(p) == 5:
        value = "%s[%s]" % (p[1],p[3])
        p[0] = Node("index", None, value)
