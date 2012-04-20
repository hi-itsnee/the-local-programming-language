# Filename:              expr.py
# Author:                Team 13
# Description:           local parser exressions
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-20 14:33:14 plt>

from localast import Node

def p_atom(p):
    '''atom : ID
            | NUMBER
            | BOOL
            | NULL
            | STRING'''
#           | COORD'''
    p[0] = Node("atom", None, p[1])

def p_expr(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr POWER expr
            | expr OR expr
            | expr AND expr
            | NOT expr
            | LPAREN expr RPAREN
            | atom'''
    # ATOM
    if len(p) == 2:
        p[0] = Node("expr", [p[1]])
    # BINOP or parenthesis
    elif len(p) == 4:
        if p[2] == '+':
            p[0] = Node("add", [p[1], p[3]], None, "%s + %s")
        elif p[2] == '-':
            p[0] = Node("subract", [p[1], p[3]], None, "%s - %s")
        elif p[2] == '*':
            p[0] = Node("multiply", [p[1], p[3]], None, "%s * %s")
        elif p[2] == '/':
            p[0] = Node("divide", [p[1], p[3]], None, "%s / %s")
        elif p[2] == '^':
            p[0] = Node("exponent", [p[1], p[3]], None, "%s ^ %s")
        # Parenthesis
        else:
            p[0] = Node("parens", [p[2]], None, "(%s)")
    # NOT
    elif len(p) == 3:
        p[0] = Node("not", [p[2]], None, "not %s")
