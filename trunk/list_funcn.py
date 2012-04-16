# Filename:                list_funcn.py
# Author:                  Team 13
# Description:             local language parser list functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-15 22:56:17 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_list_funcn(p):
    '''list_funcn : append
                  | remove
                  | pop'''
    p[0] = Node("list_funcn", [p[1]])

# APPEND
def p_append_gen(p):
    '''append : append_str
              | append_other'''
    p[0] = Node("append", [p[1]])

def p_append_str(p):
    '''append_str : APPEND LPAREN ID COMMA STRING RPAREN SEMI'''
    value = "%s.append(\"%s\")" % (p[3], p[5])
    p[0] = Node("append", None, value)

def p_append_other(p):
    '''append_other : APPEND LPAREN ID COMMA ID RPAREN SEMI
                    | APPEND LPAREN ID COMMA NUMBER RPAREN SEMI'''
    value = "%s.append(%s)" % (p[3], p[5])
    p[0] = Node("append", None, value)

# REMOVE
def p_remove(p):
    '''remove : remove_str
              | remove_other'''
    p[0] = Node("remove", [p[1]])

def p_remove_str(p):
    '''remove_str : REMOVE LPAREN ID COMMA STRING RPAREN
                  | REMOVE LPAREN ID COMMA STRING RPAREN SEMI'''
    value = "%s.remove(\"%s\")" % (p[3], p[5])
    p[0] = Node("remove", None, value)

def p_remove_other(p):
    '''remove_other : REMOVE LPAREN ID COMMA ID RPAREN
                    | REMOVE LPAREN ID COMMA ID RPAREN SEMI
                    | REMOVE LPAREN ID COMMA NUMBER RPAREN
                    | REMOVE LPAREN ID COMMA NUMBER RPAREN SEMI'''
    value = "%s.remove(%s)" % (p[3], p[5])
    p[0] = Node("remove", None, value)

# POP
def p_pop(p):
    '''pop : pop_default
           | pop_arg'''
    p[0] = Node("pop", [p[1]])

def p_pop_default(p):
    '''pop_default : POP LPAREN ID RPAREN
                   | POP LPAREN ID RPAREN SEMI'''
    value = "%s.pop()" % (p[3])
    p[0] = Node("pop", None, value)

def p_pop_arg(p):
    '''pop_arg : POP LPAREN ID COMMA NUMBER RPAREN
               | POP LPAREN ID COMMA NUMBER RPAREN SEMI'''
    value = "%s.pop(%s)" % (p[3], p[5])
    p[0] = Node("pop", None, value)
