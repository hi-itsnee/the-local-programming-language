# Filename:              expr.py
# Author:                Team 13
# Description:           local parser exressions
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-20 18:35:43 plt>

from localast import Node

def p_expr(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr MODULO expr
            | expr POWER expr
            | expr OR expr
            | expr AND expr
            | LPAREN expr RPAREN
            | NOT expr
            | MINUS expr %prec UMINUS
            | atom'''
    # BINOP or parenthesis
    if len(p) == 4:
        if p[2] == '+':
            p[0] = Node("plus", [p[1], p[3]], None, "%s + %s")
        elif p[2] == '-':
            p[0] = Node("minus", [p[1], p[3]], None, "%s - %s")
        elif p[2] == '*':
            p[0] = Node("times", [p[1], p[3]], None, "%s * %s")
        elif p[2] == '/':
            p[0] = Node("divide", [p[1], p[3]], None, "%s / %s")
        elif p[2] == '%':
            p[0] = Node("modulo", [p[1], p[3]], None, "%s %% %s")
        elif p[2] == '^':
            p[0] = Node("power", [p[1], p[3]], None, "%s ** %s")
        elif p[2] == 'or':
            p[0] = Node("or", [p[1], p[3]], None, "%s or %s")
        elif p[2] == 'and':
            p[0] = Node("and", [p[1], p[3]], None, "%s and %s")
        # Parenthesis
        else:
            p[0] = Node("parens", [p[2]], None, "(%s)")
    # NOT
    elif len(p) == 3:
        if p[1] == "not":
            p[0] = Node("not", [p[2]], None, "not %s")
        elif p[1] == "-":
            p[0] = Node("uminus", [p[2]], None, "-%s")
    # ATOM
    elif len(p) == 2:
        p[0] = Node("molecule", [p[1]])

def p_atom(p):
    '''atom : ID
            | NUMBER
            | BOOL
            | NULL
            | STRING'''
#           | LIST'''
#           | COORD'''
    p[0] = Node("atom", None, p[1])
