# Filename:                localparse.py
# Author:                  Team 13
# Description:             The local programming language parser
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-03-28 17:33:27 mc>

import ply.yacc as yacc
import locallex
from io_statement import *
from string_statement import *
from list_statement import *
from except_statement import *
from coord_statement import *
from iter_statement import *
from cond_statement import *
from math_statement import *
from logic_statement import *
from assign_statement import *
from def_statement import *
from exit_statement import *

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
               | io_statement
               | string_statement
               | list_statement
               | except_statement
               | coord_statement
               | iter_statement
               | cond_statement
               | math_statement
               | logic_statement
               | assign_statement
               | def_statement
               | exit_statement
               '''

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
Welcome to Ubuntu 11.10 (GNU/Linux 3.0.0-16-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
Last login: Wed Mar 28 17:15:38 2012 from 172.16.248.1
plt@plt:~$ tramp_exit_status 0
///e93b924d0f68d29db0ed3160dbf7d71a#$
