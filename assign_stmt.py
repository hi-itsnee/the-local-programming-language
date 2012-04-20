# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-19 22:00:31 plt>

from localast import Node
from localast import var_names

def p_assign_stmt(p):
    '''assign_stmt : ID EQUALS expr SEMI'''
    line = "%s = %s\n" % (p[1], "%s")
    p[0] = Node("assign", [p[3]], None, line)
    var_names[p[1]] = p[3]
