# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-18 21:18:52 plt>

from localast import Node

def p_assign_stmt(p):
    '''assign_stmt : ID EQUALS expr SEMI'''
    line = "%s = %s\n" % (p[1], "%s")
    p[0] = Node("assign", [p[3]], None, line)
