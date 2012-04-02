# Filename:                string_statement.py
# Author:                  Team 13
# Description:             local language parser string statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-01 21:06:09 plt>

from localast import Node
# Node(type, children=None, value=None, indent_next=False)

def p_string_statement(p):
    '''string_statement : print_statement'''
    p[0] = Node("string_statement", [p[1]])

def p_print_statement(p):
    '''print_statement : PRINT LPAREN STRING RPAREN SEMI'''
    value = "print \"%s\"" % p[3]
    p[0] = Node("print", None, value)
