# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-18 17:23:52 plt>

from localast import Node
from math_expr import *
from logic_expr import *
#from relop_expr import *
#from defcall import *

def p_assign_stmt(p):
    '''assign_stmt : ID EQUALS expr_stmt SEMI'''
#		   | ID EQUALS atom SEMI'''
    line = "%s = %s" % (p[1], "%s")
    p[0] = Node("assign", [p[3]], None, line)

def p_expr_stmt(p):
    '''expr_stmt : math_expr
		 | logic_expr'''
#		 | relop_expr
#		 | defcall'''
    p[0] = Node("expression", [p[1]])

# def p_atom(p):
#     '''atom : ID
# 	    | NUMBER
# 	    | BOOL'''
# #	    | STRING
# #	    | NULL
# #	    | COORD'''
#     value = p[1]
#     p[0] = Node("atom", None, value)
