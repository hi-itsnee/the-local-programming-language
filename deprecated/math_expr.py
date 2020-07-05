# Filename:              math_statement.py
# Author:                Team 13
# Description:           local parser math statements
# Supported Language(s): Python 3.x
# Time-stamp:            <2012-04-19 23:43:49 plt>

from localast import Node
from localast import var_names


def p_math_expr(p):
    '''math_expr : math_expr PLUS math_term
                 | math_expr MINUS math_term
                 | math_term'''
    if len(p) == 2:
        p[0] = Node("math_expression", [p[1]])
    elif len(p) == 4:
        if p[2] == '+':
            p[0] = Node("math_expression", [p[1], p[3]], None, "%s + %s")
        elif p[2] == '-':
            p[0] = Node("math_expression", [p[1], p[3]], None, "%s - %s")


def p_math_term(p):
    '''math_term : math_term TIMES math_factor
                 | math_term DIVIDE math_factor
                 | math_factor'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = Node("math_term", [p[1], p[3]], None, "%s * %s")
        elif p[2] == '/':
            p[0] = Node("math_term", [p[1], p[3]], None, "%s / %s")
    elif len(p) == 2:
        p[0] = Node("math_term", [p[1]])


def p_math_factor(p):
    '''math_factor : LPAREN math_expr RPAREN
                   | math_factor POWER math_expr
                   | ID
                   | NUMBER'''
    #                  | UMINUS math_factor '''
    #                  | math_factor MODULO math_expr

    if len(p) == 4:
        if p[1] == '(':
            p[0] = Node("math_factor", [p[2]], None, "(%s)")
        #       elif p[2] == '%':
        #           p[0] = Node("math_factor", [p[1], p[3]], None,"%s '%' %s" )
        elif p[2] == '^':
            p[0] = Node("math_factor", [p[1], p[3]], None, "%s ^ %s")
    if len(p) == 2:
        p[0] = Node("math_factor", None, p[1])

# def p_mod_factor(p):
#    '''mod_factor : MODULO '''
#    value = "%"
#    p[0] = Node("math_factor",None, value, value)
