# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 3.x
# Time-stamp:            <2012-05-05 15:09:17 plt>

from localast import Node


def p_assign_stmt(p):
    '''assign_stmt : arglist EQUALS expr
                   | arglist TIMESEQUAL expr
                   | arglist DIVEQUAL expr
                   | arglist MODEQUAL expr
                   | arglist PLUSEQUAL expr
                   | arglist MINUSEQUAL expr'''
    p[0] = Node("assign_stmt", [p[1], p[3]], p[2])
