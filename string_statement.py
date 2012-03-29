# Filename:                string_statement.py
# Author:                  Team 13
# Description:             local language parser string statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-03-28 19:49:16 plt>

from localparse_util import print_code

def p_string_statement(p):
    '''string_statement : print_statement'''

def p_print_statement(p):
    '''print_statement : PRINT LPAREN STRING RPAREN SEMI'''
    code = "print \"%s\"" % p[3]
    print_code(code, 0)
