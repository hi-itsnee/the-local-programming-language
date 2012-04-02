# Filename:                io_statement.py
# Author:                  Team 13
# Description:             local parser I/O statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-01 21:06:38 plt>

from localast import Node
# Node(type, children=None, value=None, indent_next=False)

def p_io_statement(p):
    '''io_statement : open_statement'''
    p[0] = Node("io_statement", [p[1]])

def p_open_statement(p):
    '''open_statement : OPEN LPAREN STRING RPAREN SEMI
                      | OPEN LPAREN STRING COMMA STRING RPAREN SEMI'''
    filename = p[3]
    if len(p) == 6:
        # Default is read (r)
        mode = "r"
    elif len(p) == 8:
        mode = p[5]
    value = "open(\"%s\", \"%s\")" % (filename, mode)
    p[0] = Node("open", None, value)
