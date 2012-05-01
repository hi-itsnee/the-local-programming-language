# Filename:                io_statement.py
# Author:                  Team 13
# Description:             local parser I/O statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-01 11:04:57 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_io_stmt(p):
    '''io_stmt : open_stmt
               | print_stmt
               | read_stmt'''
    p[0] = Node("io_stmt", [p[1]])

def p_open_stmt(p):
    '''open_stmt : OPEN LPAREN STRING RPAREN
                 | OPEN LPAREN STRING COMMA STRING RPAREN'''
    filename = p[3]
    if len(p) == 6:
        # Default is read (r)
        mode = "r"
    elif len(p) == 8:
        mode = p[5]
    value = "open(\"%s\", \"%s\")" % (filename, mode)
    p[0] = Node("open", None, value)

# PRINT grammar in print_stmt.py

def p_read_stmt(p):
    '''read_stmt : READ LPAREN RPAREN'''

    p[0] = Node("read_stmt", None, "raw_input()")
