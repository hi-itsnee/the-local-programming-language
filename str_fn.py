# Filename:                str_fn.py
# Author:                  Team 13
# Description:             local parser string functions
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 15:14:48 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_str_fn(p):
    '''str_fn : len
              | split
              | strip
              | str'''
    p[0] = Node("str_fn", [p[1]])

#LEN
def p_len(p):
    '''len : LEN LPAREN atom RPAREN'''
    p[0] = Node("len", [p[3]], None, "len(%s)")

#SPLIT
def p_split(p):
    '''split : SPLIT LPAREN atom COMMA atom RPAREN'''
    p[0] = Node("split", [p[3],p[5]], None, "%s.split(%s)")

#STRIP
def p_strip(p):
    '''strip : STRIP LPAREN atom COMMA atom RPAREN
             | STRIP LPAREN atom RPAREN'''
    if len(p) == 7:
        p[0] = Node("strip", [p[3],p[5]], None, "%s.strip(%s)")
    else:
        p[0] = Node("strip", [p[3]], None, "%s.strip()")

#STR
def p_str(p):
    '''str : STR LPAREN atom RPAREN'''
    p[0] = Node("str", [p[3]], None, "str(%s)")
