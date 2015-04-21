# Filename:                def_stmt.py
# Author:                  Team 13
# Description:             local parse def statement
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-05 16:29:35 plt>

from localast import Node

def p_def_stmt(p):
    '''def_stmt : DEF def_fn LBRACE stmt_list RBRACE'''
    p[0] = Node("def", [p[2], p[4]])

def p_def_fn(p):
    '''def_fn : ID LPAREN RPAREN
              | ID LPAREN arglist RPAREN
              | ID COORD'''
    if len(p) == 4:
        value = (p[1],)
        p[0] = Node("def_fn", None, value)
    elif len(p) == 5:
        p[0] = Node("def_fn", [p[3]], p[1])
    elif len(p) == 3:
        # COORD hack
        value = (p[1], p[2])
        p[0] = Node("def_fn", None, value)

# Note: arglist also used in print_stmt.py and assign_stmt.py
def p_arglist(p):
    '''arglist : arglist COMMA atom
               | atom'''
    if len(p) == 4:
        p[0] = Node("arglist", [p[1], p[3]])
    elif len(p) == 2:
        p[0] = Node("arglist", [p[1]])
