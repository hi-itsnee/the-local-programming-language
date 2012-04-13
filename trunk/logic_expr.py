# Filename:		logic_statement.py
# Author:               Team 13
# Description:          local parser logic statements
# Supported Language(s):Python 2.x

from localast import Node

def p_logic_expr(p):
    '''logic_expr : logic_expr OR logic_term
		  | logic_term'''
    if len(p) == 2:
        p[0] = Node("logic_expression",[p[1]], None, "%s")
    elif len(p) == 4:
        p[0] = Node("logic_expression",[p[1],p[3]], None, "%s or %s")

def p_logic_term(p):
    '''logic_term : logic_term AND logic_factor
		  | logic_factor'''

    if len(p) == 2:
        p[0] = Node("logic_term",[p[1]],None,"%s")
    elif len(p) == 4:
        p[0] = Node("logic_term",[p[1],p[3]],None,"%s and %s")

def p_logic_factor(p):
    '''logic_factor : LPAREN logic_expr RPAREN
		    | NOT logic_factor
		    | ID
		    | BOOL '''
    if len(p) == 4:
	p[0] = Node("logic_factor",[p[2]],None,"(%s)")
    elif len(p) == 3:
	p[0] = Node("logic_factor",[p[2]],None,"not %s")
    elif len(p) == 2:
	value = "%s" % (p[1])
    	p[0] = Node("logic_factor",None, value, value)
