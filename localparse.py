# Filename:                localparse.py
# Author:                  Team 13
# Description:             The local programming language parser
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-19 23:10:14 plt>

import ply.yacc as yacc
import locallex
from io_stmt import *
from print_stmt import *
#from except_stmt import *
#from coord_stmt import *
#from iter_stmt import *
from cond_stmt import *
from assign_stmt import *
from def_stmt import *
from exit_stmt import *
from expr import *
from math_expr import *
from logic_expr import *
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
    ('left','POWER')
    # ('left','MODULO')
    # ('right','UMINUS')
    )

def p_program(p):
    '''program : program stmt_list
               | stmt_list'''
    if len(p) == 3:
        p[0] = Node("program", [p[1], p[2]])
    elif len(p) == 2:
        p[0] = Node("program", [p[1]])

def p_stmt_list(p):
    '''stmt_list : stmt_list stmt
                 | stmt'''
    if len(p) == 3:
        p[0] = Node("statement_list", [p[1], p[2]])
    elif len(p) == 2:
        p[0] = Node("statement_list", [p[1]])

def p_stmt(p):
    '''stmt : io_stmt
            | assign_stmt
            | cond_stmt
            | print_stmt
            | exit_stmt
            | def_stmt'''
          # | except_stmt
          # | iter_stmt
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

def parse(data, debug=False):
    lparser.error = 0
    p = lparser.parse(data, debug=debug) # The AST
    if lparser.error:
        return None
    return p
