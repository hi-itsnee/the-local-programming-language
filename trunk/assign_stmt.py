# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-20 16:03:52 plt>

from localast import Node

def p_assign_stmt(p):
    '''assign_stmt : ID EQUALS expr SEMI'''
    p[0] = Node("assign", [p[3]], p[1])
