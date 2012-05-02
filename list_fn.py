# Filename:                list_fn.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 10:44:43 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_list_fn(p):
    '''list_fn : append
               | remove_generic
               | pop_generic'''
    p[0] = Node("list_fn", [p[1]])

# APPEND - Appends item to end of list
def p_append(p):
    '''append : APPEND LPAREN atom COMMA atom RPAREN SEMI'''
    p[0] = Node("append", [p[3], p[5]], None, "%s.append(%s)")
    # MUST ADD AST ACTION

# REMOVE - Removes (and returns) specified item from list
def p_remove_generic(p):
    '''remove_generic : remove
                      | remove SEMI'''
    p[0] = Node("remove_generic", [p[1]])

def p_remove_expr(p):
    '''remove : REMOVE LPAREN atom COMMA atom RPAREN'''
    # Can be used in assignment stmt or alone
    p[0] = Node("remove", [p[3], p[5]], None, "%s.remove(%s)")
    # MUST ADD AST ACTION

# POP - Removes (and returns) item from specified position in list
def p_pop_generic(p):
    '''pop_generic : pop_assignment
                   | pop SEMI'''
    #Note : Previous production of pop_generic -> pop(for assignment) was being considered as pop SEMI(stand alone); thus causing an error while parsing
    p[0] = Node("pop_generic", [p[1]])

def p_pop_assignment(p):
    '''pop_assignment : POP LPAREN atom RPAREN
                      | POP LPAREN atom COMMA atom RPAREN'''
    if len(p) == 5:
        p[0] = Node("pop_assignment", [p[3]], None, "%s.pop()")
    else:    
        p[0] = Node("pop_assignment", [p[3], p[5]], None, "%s.pop(%s)")

def p_pop(p):
    '''pop : POP LPAREN atom RPAREN
           | POP LPAREN atom COMMA atom RPAREN'''
    if len(p) == 5:
        p[0] = Node("pop", [p[3]], None, "%s.pop()")
    elif len(p) == 7:
        p[0] = Node("pop", [p[3], p[5]], None, "%s.pop(%s)")
    # MUST ADD AST ACTION
