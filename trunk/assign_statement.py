# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-03-31 02:00:00>

from localast import Node

def p_assign_statement(p): 
    '''assign_statement : ID EQUALS ID SEMI
                        | ID EQUALS NUMBER SEMI'''

    value = "%s = %s" % (p[1], p[3])
    # Setup the AST Walk:
    p[0] = Node("assign", None, value, value)

