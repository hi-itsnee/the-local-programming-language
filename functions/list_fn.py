# Filename:                list_fn.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 10:44:43 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_list_fn(p):
    '''list_fn : append
               | remove
               | pop'''
    p[0] = Node("list_fn", [p[1]])

# APPEND - Appends item to end of list
def p_append(p):
    '''append : APPEND LPAREN atom COMMA atom RPAREN'''
    p[0] = Node("append", [p[3], p[5]], None, "%s.append(%s)")

# REMOVE - Removes (and returns) specified item from list
def p_remove(p):
    '''remove : REMOVE LPAREN atom COMMA atom RPAREN'''
    p[0] = Node("remove", [p[3],p[5]], None, "%s.remove(%s)")

# POP - Removes (and returns) item from specified position in list
def p_pop(p):
    '''pop : POP LPAREN atom RPAREN
           | POP LPAREN atom COMMA atom RPAREN'''
    if len(p) == 5:
        p[0] = Node("pop", [p[3]], None, "%s.pop()")
    elif len(p) == 7:
        p[0] = Node("pop", [p[3], p[5]], None, "%s.pop(%s)")
