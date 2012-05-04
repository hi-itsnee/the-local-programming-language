# Filename:              atom.py
# Author:                Team 13
# Description:           local parser atoms
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-05-04 16:40:33 plt>

from localast import Node

def p_atom(p):
    '''atom : ID
            | NUMBER
            | BOOL
            | NULL
            | COORD
            | STRING
            | LIST'''
    p[0] = Node("atom", None, p[1])
