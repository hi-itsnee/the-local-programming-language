# Filename:                localparse.py
# Author:                  Team 13
# Description:             The local programming language parser
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-02 22:34:56 plt>

import ply.yacc as yacc
import locallex
from io_stmt import *
from print_stmt import *
from except_stmt import *
from cond_stmt import *
from assign_stmt import *
from def_stmt import *
from exit_stmt import *
from iter_stmt import *
from expr import *
from jump_stmt import *
from list_fn import *
from coord_fn import *
from str_fn import *
from atom import *
from argv_fn import *
from double_stmt import *

from localast import Node
# Node(type, children=None, value=None, line=None)

# The tokens from our lexer
tokens = locallex.tokens

# The first rule
start = 'program'

# Operator precendence and associativity
precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELIF'),
    ('nonassoc', 'ELSE'),
    ('left', 'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL',
     'MINUSEQUAL', 'ANDEQUAL', 'OREQUAL'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right','NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('left', 'PLUSPLUS', 'MINUSMINUS'),
    ('left','POWER'),
    ('right','UMINUS')
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
        p[0] = Node("stmt_list", [p[1], p[2]], None, "%s")
    elif len(p) == 2:
        p[0] = Node("stmt_list", [p[1]], None, "%s\n")

def p_stmt(p):
    '''stmt : io_stmt SEMI
            | assign_stmt SEMI
            | cond_stmt
            | exit_stmt SEMI
            | def_stmt
            | iter_stmt
            | jump_stmt SEMI
            | list_fn SEMI
            | except_stmt
            | double_stmt SEMI'''
    p[0] = Node("statement", [p[1]], None, "%s")

# Error handler
def p_error(p):
    if not p:
        print("Catastrophic error in your code. I cannot help you.")
    else:
        print "Syntax error at line %s near %s" % (p.lineno, p.value)
        yacc.restart()

# The PLY parser (internally runs the lexer)
lparser = yacc.yacc()

def parse(data, debug=False):
    lparser.error = 0
    p = lparser.parse(data, debug=debug) # The AST
    if lparser.error:
        return None
    return p
