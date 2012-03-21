# Filename:                localparse.py
# Author:                  Team 13
# Description:             The local programming language parser
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-03-21 16:59:37 mc>

import ply.yacc as yacc
import locallex
from io_statement import *

# Enable/disable debugging
DEBUG = True

# The tokens from our lexer
tokens = locallex.tokens

# The first rule
start = 'program'

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
