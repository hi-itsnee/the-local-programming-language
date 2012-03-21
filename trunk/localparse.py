# Filename:                localparse.py
# Author:                  Team 13
# Description:             The local programming language parser
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-03-20 22:56:03 mc>

import ply.yacc as yacc
import locallex

# Send semantically equivalent Python code to stdout
emit_code = True

# Enable/disable debugging
DEBUG = True

# The tokens from our lexer
tokens = locallex.tokens

# Number of spaces a tab equals
INDENT = 4

precedence = (
    # ('left', 'PLUS','MINUS'),
    # ('left', 'TIMES','DIVIDE'),
    # ('left', 'POWER'),
    # ('right','UMINUS')
    )

def p_program(p):
    '''program : program io_statement
               | io_statement'''

# Error handler. Return nothing.
def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1

def p_io_statement(p):
    '''io_statement : print_statement'''

def p_print_statement(p):
    '''print_statement : PRINT LPAREN STRING RPAREN SEMI'''
    code = "print \"%s\"" % p[3]
    print_code(code, 0)

# Catastrophic error handler
def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")

lparser = yacc.yacc()

def parse(data, debug=DEBUG):
    lparser.error = 0
    p = lparser.parse(data, debug=debug)
    if lparser.error:
        return None
    return p

def print_code(code, indent):
    indent *= INDENT
    if not emit_code:
        return
    codelines = code.splitlines()
    for c in codelines:
        print "%s%s" % (" "*indent, c)
