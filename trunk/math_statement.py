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
                 | NUMBER POWER NUMBER'''

    if p[2] == '+':
        p[0] = Node("plus", None, "%s + %s" % (p[1], p[3]))
    # elif p[2] == '-':
    #     if (p[1] == ID and p[3] == ID):
    #         p[0] = Node("math", [p[1], p[3]], None, "%s - %s;\n")
    #     elif (p[1] == NUMBER and p[3] == NUMBER):
    #         p[0] = p[1] - p[3]
    #     else: print 'The minus operator received bad inputs\n'	    
    # elif p[2] == '*':
    #     if (p[1] == ID and p[3] == ID):
    #         p[0] = Node("math", [p[1], p[3]], None, "%s * %s;\n")
    #     elif (p[1] == NUMBER and p[3] == NUMBER):
    #         p[0] = p[1] * p[3]
    #     else: print 'The times operator received bad inputs\n'
    # elif p[2] == '/':
    #     if (p[1] == ID and p[3] == ID):
    #         p[0] = Node("math", [p[1], p[3]], None, "%s / %s;\n")
    #     elif (p[1] == NUMBER and p[3] == NUMBER):
    #         p[0] = p[1] / p[3]
    #     else: print 'The divide operator received bad inputs\n'
    # elif p[2] == '^':
    #     if (p[1] == ID and p[3] == ID):
    #         p[0] = Node("math", [p[1], p[3]], None, "%s ^ %s;\n")
    #     elif (p[1] == NUMBER and p[3] == NUMBER):
    #         p[0] = p[1] ** p[3]
    #     else: print 'The power operator received bad inputs\n'
