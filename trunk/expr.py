# Filename:              expr.py
# Author:                Team 13
# Description:           local parser exressions
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-18 20:56:47 plt>

from localast import Node
from math_expr import *
from logic_expr import *
#from relop_expr import *
#from defcall import *

def p_expr(p):
    '''expr : atom
            | math_expr
	    | logic_expr'''
#	    | relop_expr
#	    | defcall'''
    p[0] = Node("expression", [p[1]])

def p_atom(p):
    '''atom : ID
	    | NUMBER
	    | BOOL'''
#	    | STRING
#	    | NULL
#	    | COORD'''
    value = p[1]
    p[0] = Node("atom", None, value)
