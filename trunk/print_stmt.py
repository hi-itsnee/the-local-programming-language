# Filename:                print_stmt.py
# Author:                  Team 13
# Description:             local parser print statement
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-29 21:41:22 plt>

from localast import Node
#Node(type, children=Node, value=None, line=None)

def p_print_stmt(p):
    '''print_stmt : simple_print_stmt
                  | format_print_stmt'''
    p[0] = Node("print_stmt", [p[1]])

def p_simple_print_stmt(p):
    '''simple_print_stmt : PRINT LPAREN atom RPAREN SEMI'''
    p[0] = Node("print", [p[3]])

def p_format_print_stmt(p):
    '''format_print_stmt : PRINT LPAREN atom COMMA arglist RPAREN SEMI'''
    # Note: arglist defined in def_stmt.py
    p[0] = Node("print", [p[3], p[5]])
