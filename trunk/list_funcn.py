# Filename:                list_funcn.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-20 19:07:10 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_list_funcn(p):
    '''list_funcn : append
                  | remove_generic
                  | pop_generic'''
    p[0] = Node("list_funcn", [p[1]])

# APPEND - Appends item to end of list
def p_append(p):
    '''append : APPEND LPAREN atom COMMA atom RPAREN SEMI'''
    p[0] = Node("append", [p[3], p[5]])
    # MUST ADD AST ACTION

# REMOVE - Removes (and returns) specified item from list
def p_remove_generic(p):
    '''remove_generic : remove
                      | remove SEMI'''
    p[0] = Node("remove_generic", [p[1]])

def p_remove_expr(p):
    '''remove : REMOVE LPAREN atom COMMA atom RPAREN'''
    # Can be used in assignment stmt or alone
    p[0] = Node("remove", [p[3], p[5]])
    # MUST ADD AST ACTION

# POP - Removes (and returns) item from specified position in list
def p_pop_generic(p):
    '''pop_generic : pop
                   | pop SEMI'''
    p[0] = Node("pop_generic", [p[1]])

def p_pop(p):
    '''pop : POP LPAREN atom RPAREN
           | POP LPAREN atom COMMA atom RPAREN'''
    if len(p) == 5:
        p[0] = Node("pop", [p[3]])
    elif len(p) == 7:
        p[0] = Node("pop", [p[3], p[5]])
    # MUST ADD AST ACTION
