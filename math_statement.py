# Filename:              math_statement.py
# Author:                Team 13
# Description:           local parser math statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-04 17:53:48 plt>

from localast import Node

def p_math_statement(p):
    '''math_statement : math_statement PLUS math_term
		      | math_statement MINUS math_term
		      | math_term'''
    if len(p) == 2:
        p[0] = Node("math_statement", [p[1]], None, "%s")
    elif len(p) == 4:
        if p[2] == '+':
            p[0] = Node("math_statement", [p[1],p[3]], None, "%s + %s")
        elif p[2] == '-':
            p[0] = Node("math_statement", [p[1],p[3]], None, "%s - %s")

def p_math_term(p):
    '''math_term : math_term TIMES math_factor
                 | math_term DIVIDE math_factor
		 | math_factor'''
   
    if len(p) == 4:
	if p[2] == '*':
	    p[0] = Node("math_term", [p[1],p[3]], None, "%s * %s")
	elif p[2] == '/':
	    p[0] = Node("math_term", [p[1],p[3]], None, "%s / %s")
    elif len(p) == 2:
	p[0] = Node("math_term", [p[1]], None, "%s")

def p_math_factor(p):
    '''math_factor : LPAREN math_statement RPAREN
                   | math_factor MODULO math_statement
		   | math_factor POWER math_statement
		   | ID'''
#		   | UMINUS math_factor '''

    if len(p) == 4:
	if p[1] == '(':
            p[0] = Node("math_factor", [p[2]], None, "(%s)")
	elif p[2] == '%':
	    p[0] = Node("math_factor", [p[1],p[3]], None, "%s % %s")
	elif p[2] == '^':
	    p[0] = Node("math_factor", [p[1],p[3]], None, "%s ^ %s")
    if len(p) == 2:
       value = "%s" % (p[1])
       p[0] = Node("math_factor",None, value, value)
