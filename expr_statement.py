# Filename:                expr_statement.py
# Author:                  Team 13
# Description:             local language parser expression statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-02 16:57:27 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_expr_statement(p):
    '''expr_statement : ID
                      | LPAREN ID RPAREN'''
    if len(p) == 2:
        p[0] = Node("expr", None, p[1])
    elif len(p) == 4:
        p[0] = Node("expr", None, p[2])
