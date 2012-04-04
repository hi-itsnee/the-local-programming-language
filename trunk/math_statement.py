# Filename:              math_statement.py
# Author:                Team 13
# Description:           local parser math statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-04 10:00:00>

from localast import Node

def p_math_statement(p): 
# TO DO: FIX FOR ORDER OF PRECEDENCE
#        FIX FOR NUMBERS ALSO INSTEAD OF ONLY IDs
    '''math_statement : ID EQUALS ID POWER ID SEMI
                      | ID EQUALS ID PLUS ID SEMI
                      | ID EQUALS ID MINUS ID SEMI
                      | ID EQUALS ID TIMES ID SEMI
                      | ID EQUALS ID DIVIDE ID SEMI'''


    if p[4] == "POWER":
        p[0] = Node("math", None, pow(p[3], p[5]))
    elif p[4] == "PLUS":
        p[0] = Node("math", None, p[3] + p[5])
    elif p[4] == "MINUS":
        p[0] = Node("math", None, p[3] - p[5])  
    elif p[4] == "TIMES":
        p[0] = Node("math", None, p[3] * p[5])
    elif p[4] == "DIVIDE":
        p[0] = Node("math", None, p[3] / p[5])    
