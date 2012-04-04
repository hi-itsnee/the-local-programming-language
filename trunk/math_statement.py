# Filename:              math_statement.py
# Author:                Team 13
# Description:           local parser math statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-04 10:00:00>

from localast import Node

def p_math_statement(p): 
    '''math_statement : ID EQUALS math_expr''' 

    value = "%s = " % (p[1])
    p[0] = Node("math_expr", p[1], value, None)


def p_math_expr(p):
    '''math_expr : NUMBER PLUS NUMBER SEMI
                 | NUMBER MINUS NUMBER SEMI
                 | NUMBER TIMES NUMBER SEMI
                 | NUMBER DIVIDE NUMBER SEMI
                 | NUMBER POWER NUMBER SEMI
                 | ID'''

    if p[2] == '+':
        if (p[1] == ID and p[3] == ID):
            p[0] = Node("math", [p[1], p[3]], None, "%s + %s;\n")
        elif (p[1] == NUMBER and p[3] == NUMBER):
            p[0] = p[1] + p[3]
	else: print "The plus operator received bad inputs\n"
    elif p[2] == '-':
        if (p[1] == ID and p[3] == ID):
            p[0] = Node("math", [p[1], p[3]], None, "%s - %s;\n")
        elif (p[1] == NUMBER and p[3] == NUMBER):
            p[0] = p[1] - p[3]
	else: print 'The minus operator received bad inputs\n'	    
    elif p[2] == '*':
        if (p[1] == ID and p[3] == ID):
            p[0] = Node("math", [p[1], p[3]], None, "%s * %s;\n")
        elif (p[1] == NUMBER and p[3] == NUMBER):
            p[0] = p[1] * p[3]
	else: print 'The times operator received bad inputs\n'
    elif p[2] == '/':
        if (p[1] == ID and p[3] == ID):
            p[0] = Node("math", [p[1], p[3]], None, "%s / %s;\n")
        elif (p[1] == NUMBER and p[3] == NUMBER):
            p[0] = p[1] / p[3]
	else: print 'The divide operator received bad inputs\n'
    elif p[2] == '^':
        if (p[1] == ID and p[3] == ID):
            p[0] = Node("math", [p[1], p[3]], None, "%s ^ %s;\n")
        elif (p[1] == NUMBER and p[3] == NUMBER):
            p[0] = p[1] ** p[3]
	else: print 'The power operator received bad inputs\n'
