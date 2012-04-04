# Filename:                localparse.py
# Author:                  Team 13
# Description:             The local programming language parser
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-02 16:56:12 plt>

import ply.yacc as yacc
import locallex
from io_statement import *
from string_statement import *
#from list_statement import *
#from except_statement import *
from coord_statement import *
#from iter_statement import *
from cond_statement import *
from math_statement import *
from logic_statement import *
from assign_statement import *
#from def_statement import *
#from exit_statement import *
from expr_statement import *

from localast import Node
# Node(type, children=None, value=None, line=None)

# Enable/disable debugging
DEBUG = False

# The tokens from our lexer
tokens = locallex.tokens

# The first rule
start = 'program'

# Operator precendence and associativity
precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('left', 'AND','OR'),
    ('right','NOT'),
    ('left', 'PLUS','MINUS'),
    ('left', 'TIMES','DIVIDE'),
    ('left', 'POWER')
    # ('right','UMINUS')
    )

def p_program(p):
    '''program : program statement_list
               | statement_list'''
    if len(p) == 3:
        p[0] = Node("program", [p[1], p[2]])
    elif len(p) == 2:
        p[0] = Node("program", [p[1]])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = Node("statement_list", [p[1], p[2]])
    elif len(p) == 2:
        p[0] = Node("statement_list", [p[1]])

def p_statement(p):
    '''statement : string_statement
                 | io_statement
                 | assign_statement
                 | cond_statement
                 | logic_statement
                 | math_statement
                 | expr_statement'''
               # | list_statement
               # | except_statement
               # | coord_statement
               # | iter_statement
               # | def_statement
               # | exit_statement
               # '''
    p[0] = Node("statement", [p[1]])

# Error handler. Return nothing.
def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1

# Catastrophic error handler
def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")

# The PLY parser (internally runs the lexer)
lparser = yacc.yacc()

def parse(data, debug):
    lparser.error = 0
    p = lparser.parse(data, debug=debug) # The AST
    if lparser.error:
        return None
    return p
