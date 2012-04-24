# Filename:                print_stmt.py
# Author:                  Team 13
# Description:             local parser print statement
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 13:18:16 plt>

from localast import Node
#Node(type, children=Node, value=None, line=None)

def p_print_stmt(p):
    '''print_stmt : simple_print_stmt
                  | format_print_stmt'''
    p[0] = Node("print1", [p[1]])

def p_simple_print_stmt(p):
    '''simple_print_stmt : PRINT LPAREN STRING RPAREN SEMI'''
    value = "print \"%s\"\n" % p[3]
    p[0] = Node("simpleprint", None, value)

def p_format_print_stmt(p):
    '''format_print_stmt : PRINT LPAREN STRING COMMA format_stmt RPAREN SEMI'''
    value = "print \"%s\"" % p[3]
    p[0] = Node("format_print_statement", [p[5]], value)

def p_format_stmt(p):
    '''format_stmt : format_stmt COMMA STRING
                   | STRING'''
    if len(p) == 4:
        p[0] = Node("format_statement", [p[1]], p[3], None)
    if len(p) == 2:
        value = p[1]
        p[0] = Node("format_statement", None, value)
