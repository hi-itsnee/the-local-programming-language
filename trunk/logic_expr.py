# Filename:              logic_statement.py
# Author:                Team 13
# Description:           local parser logic statements
# Supported Language(s): Python 2.x

from localast import Node
from localast import var_names

def p_logic_expr(p):
    '''logic_expr : logic_expr OR logic_term
                  | logic_term'''
    if len(p) == 2:
        p[0] = Node("logic_expression", [p[1]], None)
    elif len(p) == 4:
        p[0] = Node("logic_expression", [p[1], p[3]], None, "%s or %s")

def p_logic_term(p):
    '''logic_term : logic_term AND logic_factor
                  | logic_factor'''
    if len(p) == 2:
        p[0] = Node("logic_term", [p[1]], None)
    elif len(p) == 4:
        p[0] = Node("logic_term", [p[1], p[3]], None, "%s and %s")

def p_logic_factor(p):
    '''logic_factor : LPAREN logic_expr RPAREN
                    | NOT logic_factor
                    | ID
                    | BOOL'''
    if len(p) == 4:
        p[0] = Node("logic_factor", [p[2]], None, "(%s)")
    elif len(p) == 3:
        p[0] = Node("logic_factor", [p[2]], None, "not %s")
    elif len(p) == 2:
        if p[1] == 'true':
            value = 'True'
        elif p[1] == 'false':
            value = 'False'
        else:
            if not var_names.has_key(p[1]):
                print "Undefined variable", p[1], "in line", p.lineno(1)
                p[0] = None
                p.parser.error = 1
            else:
                value = p[1]
        p[0] = Node("variable", None, value)
