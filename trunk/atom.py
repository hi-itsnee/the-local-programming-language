# Filename:              atom.py
# Author:                Team 13
# Description:           local parser exressions
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-20 18:35:43 plt>

from localast import Node

def p_atom(p):
    '''atom : ID
            | NUMBER
            | BOOL
            | NULL
            | COORD
            | STRING'''
#           | LIST'''
#    if len(p) == 2:
    p[0] = Node("atom", None, p[1])
#    else:
#        p[0] = Node("atom",None,p[2])
