# Filename:              atom.py
# Author:                Team 13
# Description:           local parser atoms
# Supported Language(s): Python 3.x
# Time-stamp:            <2012-05-05 13:10:57 plt>

from local.localast import Node  # Node(type, children=None, value=None, line=None)


def p_atom(p):
    """atom : ID
            | NUMBER
            | BOOL
            | NULL
            | COORD
            | STRING"""
    p[0] = Node("atom", None, p[1])
