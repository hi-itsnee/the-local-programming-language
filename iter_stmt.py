# Filename:                iter_stmt.py
# Author:                  Team 13
# Description:             local parser iteration statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 12:54:41 plt>

from localast import Node

def p_iter_stmt(p):
    '''iter_stmt : while_stmt
                 | for_stmt'''

    p[0] = Node("iter", [p[1]])

def p_while_stmt(p):
    '''while_stmt : WHILE expr stmt
                  | WHILE expr LBRACE stmt_list RBRACE'''
    if len(p) == 4:
        p[0] = Node("while", [p[2], p[3]])
    else:
        p[0] = Node("while", [p[2], p[4]])

def p_for_stmt(p):
    '''for_stmt : FOR ID IN atom stmt
                | FOR ID IN atom LBRACE stmt_list RBRACE'''
    if len(p) == 6:
        p[0] = Node("for", [p[4], p[5]], p[2])
    else:
        p[0] = Node("for", [p[4], p[6]], p[2])
