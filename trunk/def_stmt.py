# Filename:                def_stmt.py
# Author:                  Team 13
# Description:             local parse def statement
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-29 19:08:32 plt>

from localast import Node

def p_def(p):
    '''def_stmt : DEF ID LPAREN arglist RPAREN LBRACE stmt_list RBRACE'''
    p[0] = Node("def", [p[4], p[7]], p[2])

def p_arglist(p):
    '''arglist : arglist COMMA atom
               | atom'''
    if len(p) == 4:
        p[0] = Node("arglist", [p[1], p[3]])
    elif len(p) == 2:
        p[0] = Node("arglist", [p[1]])
