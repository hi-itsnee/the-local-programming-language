# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-04 06:00:00>

from localast import Node
from math_expr import *
from logic_expr import *
#from relop_expr import *
#from defcall import *

def p_assign_stmt(p): 

    '''assign_stmt : identifier EQUALS expr_stmt
		   | identifier EQUALS atom SEMI'''
    if len(p) == 5:
        value = "%s = %s" % (p[1],p[3])
        p[0] = Node("assign", None, value, value)
    else:
        p[0] = Node("assign", [p[1],p[3]], None, "%s = %s")

def p_expr_stmt(p):
    '''expr_stmt : math_expr SEMI
		 | logic_expr SEMI
                 | ID'''
#		 | relop_expr
#		 | defcall'''
 
    p[0] = Node("expression", [p[1]], None, "%s")

def p_atom(p):
    '''atom : ID
	    | NUMBER'''
#	    | STRING
#	    | BOOL
#	    | NULL
#	    | COORD'''
    
    value = "%s" % (p[1])
    p[0] = Node("atom", None, value, value)

def p_identifier(p):
    '''identifier : ID'''

    value = "%s" % (p[1])
    p[0] = Node("identifier", None, value, value)
