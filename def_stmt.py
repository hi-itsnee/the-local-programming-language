# Filename:                def_stmt.py
# Author:                  Team 13
# Description:             local parse def statement
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-05 15:08:00 plt>

from localast import Node

def p_def(p):
    '''def_stmt : DEF ID LPAREN RPAREN LBRACE stmt_list RBRACE
                | DEF ID LPAREN arglist RPAREN LBRACE stmt_list RBRACE'''
    if len(p) == 8:
        p[0] = Node("def", [p[6]], p[2])
    elif len(p) == 9:
        p[0] = Node("def", [p[4], p[7]], p[2])

# Note: arglist also used in print_stmt.py and assign_stmt.py
def p_arglist(p):
    '''arglist : arglist COMMA atom
               | atom'''
    if len(p) == 4:
        p[0] = Node("arglist", [p[1], p[3]])
    elif len(p) == 2:
        p[0] = Node("arglist", [p[1]])
