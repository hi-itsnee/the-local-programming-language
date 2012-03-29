# Filename:                io_statement.py
# Author:                  Team 13
# Description:             local parser I/O statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-03-28 20:04:13 plt>

from localparse_util import print_code

def p_io_statement(p):
    '''io_statement : open_statement'''

def p_open_statement(p):
    '''open_statement : OPEN LPAREN STRING RPAREN SEMI
                      | OPEN LPAREN STRING COMMA STRING RPAREN SEMI'''
    filename = p[3]
    if len(p) == 6:
        # Default is read (r)
        mode = "r"
    elif len(p) == 8:
        mode = p[5]
    code = "open(\"%s\", \"%s\")" % (filename, mode)
    print_code(code, 0)
