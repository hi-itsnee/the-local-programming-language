# Filename:              expr.py
# Author:                Team 13
# Description:           local parser exressions
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-24 15:59:53 plt>

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
            | expr LT expr
            | expr LE expr
            | expr GT expr
            | expr GE expr
            | expr EQ expr
            | expr NE expr
            | expr LBRACKET atom RBRACKET
            | LPAREN expr RPAREN
            | atom 
            | NOT expr %prec NOT
            | MINUS expr %prec UMINUS
            | atom
            | coord_fn
            | list_fn
            | str_fn'''
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
        elif p[2] == '<':
            p[0] = Node("lt", [p[1], p[3]], None, "%s < %s")
        elif p[2] == '<=':
            p[0] = Node("le", [p[1], p[3]], None, "%s <= %s")
        elif p[2] == '>':
            p[0] = Node("gt", [p[1], p[3]], None, "%s > %s")
        elif p[2] == '>=':
            p[0] = Node("ge", [p[1], p[3]], None, "%s >= %s")
        elif p[2] == '==':
            p[0] = Node("eq", [p[1], p[3]], None, "%s == %s")
        elif p[2] == '!=':
            p[0] = Node("ne", [p[1], p[3]], None, "%s != %s")
        # Parenthesis
        else:
            p[0] = Node("parens", [p[2]], None, "(%s)")

    # Indices [#]
    elif len(p) == 5:
        p[0] = Node("array", [p[1], p[3]], None, "%s([%s])")

    # NOT
    elif len(p) == 3:
        if p[1] == "not":
            p[0] = Node("not", [p[2]], None, "not %s")
        elif p[1] == "-":
            p[0] = Node("uminus", [p[2]], None, "-%s")
    # ATOM
    elif len(p) == 2:
        p[0] = Node("molecule", [p[1]])
