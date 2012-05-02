# Filename:                io_statement.py
# Author:                  Team 13
# Description:             local parser I/O statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-02 16:44:00 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_io_stmt(p):
    '''io_stmt : print_stmt
               | close_stmt'''
    p[0] = Node("io_stmt", [p[1]])

def p_io_fn(p):
    '''io_fn : open_stmt
             | read_stmt'''
    p[0] = Node("io_fn", [p[1]])

def p_open_stmt(p):
    '''open_stmt : OPEN LPAREN STRING RPAREN
                 | OPEN LPAREN STRING COMMA STRING RPAREN'''
    filename = p[3]
    if len(p) == 5:
        # Default is read (r)
        mode = "r"
    elif len(p) == 7:
        mode = p[5]
    value = "open(%s, %s)" % (filename, mode)
    p[0] = Node("open", None, value, value)

# PRINT grammar in print_stmt.py

def p_close_stmt(p):
    '''close_stmt : CLOSE LPAREN atom RPAREN SEMI'''
    p[0] = Node("close", [p[3]], None, "%s.close()")

def p_read_stmt(p):
    '''read_stmt : READ LPAREN atom RPAREN
                 | READ LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = Node("read_stmt", [p[3]], None, "raw_input(%s)")
    elif len(p) == 4:
        p[0] = Node("read_stmt", None, "raw_input()")
