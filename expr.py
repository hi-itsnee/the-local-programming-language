# Filename:              expr.py
# Author:                Team 13
# Description:           local parser exressions
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-19 23:25:01 plt>

from localast import Node
from localast import var_names
#from relop_expr import *
#from defcall import *

def p_expr(p):
    '''expr : atom
            | math_expr
            | logic_expr'''
#           | relop_expr
#           | defcall'''
    p[0] = Node("expression", [p[1]])

def p_atom(p):
    '''atom : variable
            | number
            | boolean
            | NULL
            | STRING'''
#           | COORD'''
    p[0] = Node("atom", [p[1]])

def p_variable(p):
    '''variable : ID'''
    if not var_names.has_key(p[1]):
        print "Undefined variable", p[1], "in line", p.lineno(1)
        p[0] = None
        p.parser.error = 1
    else:
        p[0] = Node("variable", None, p[1])

def p_number(p):
    '''number : NUMBER'''
    p[0] = Node("number", None, p[1])

def p_boolean(p):
    '''boolean : BOOL'''
    if p[1] == 'true':
        value = 'True'
    if p[1] == 'false':
        value = 'False'
    p[0] = Node("boolean", None, value)
