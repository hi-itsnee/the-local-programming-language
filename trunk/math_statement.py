# Filename:              math_statement.py
# Author:                Team 13
# Description:           local parser math statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-04 17:53:48 plt>

from localast import Node

def p_math_statement(p):
    '''math_statement : ID EQUALS math_expr SEMI'''
    line = p[1] + " = %s"
    p[0] = Node("math_expr", [p[3]], None, line)


def p_math_expr(p):
    '''math_expr : NUMBER PLUS NUMBER
                 | NUMBER MINUS NUMBER
                 | NUMBER TIMES NUMBER
                 | NUMBER DIVIDE NUMBER
                 | NUMBER MODULO NUMBER
                 | NUMBER POWER NUMBER'''

    if p[2] == '+':
        p[0] = Node("plus", None, "%s + %s" % (p[1], p[3]))
    elif p[2] == '-':
        p[0] = Node("minus", None, "%s - %s" % (p[1], p[3]))
    elif p[2] == '*':
        p[0] = Node("times", None, "%s * %s" % (p[1], p[3]))
    elif p[2] == '/':
        p[0] = Node("divide", None, "%s / %s" % (p[1], p[3]))
    elif p[2] == '%':
        p[0] = Node("modulo", None, "%s % %s" % (p[1], p[3]))
    elif p[2] == '^':
        p[0] = Node("power", None, "%s ** %s" % (p[1], p[3]))
    else: 
        print 'Error in math expression\n'
