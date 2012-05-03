# Filename:                double_stmt.py
# Author:                  Team 13
# Description:             local parser double statments
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-02 17:25:28 plt>

from localast import Node

def p_double_stmt(p):
    ''' double_stmt : ID MINUSMINUS %prec MINUSMINUS
                    | ID PLUSPLUS %prec PLUSPLUS'''
    if p[2] == "++":
        value = "(%s += 1)" % (p[1])
    elif p[2] == "--":
        value = "(%s -= 1)" % (p[1])
    p[0] = Node("double", None, value)
