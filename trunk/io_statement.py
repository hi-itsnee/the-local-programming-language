# Filename:                io_statement.py
# Author:                  Team 13
# Description:             The local programming language parser I/O statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-03-21 16:59:03 mc>

from localparse_util import print_code

def p_io_statement(p):
    '''io_statement : print_statement'''

def p_print_statement(p):
    '''print_statement : PRINT LPAREN STRING RPAREN SEMI'''
    code = "print \"%s\"" % p[3]
    print_code(code, 0)
