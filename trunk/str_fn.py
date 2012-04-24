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
    '''len : len_str
           | len_id'''
    p[0] = Node("len", [p[1]], None)

def p_len_str(p):
    '''len_str : LEN LPAREN STRING RPAREN'''
    value = "len(\"%s\")" % p[3]
    p[0] = Node("len", None, value)

def p_len_id(p):
    '''len_id : LEN LPAREN ID RPAREN'''
    value = "len(%s)" % p[3]
    p[0] = Node("len", None, value)

#SPLIT
def p_split(p):
    '''split : split_str
             | split_id'''
    p[0] = Node("print", [p[1]])

def p_split_str(p):
    '''split_str : SPLIT LPAREN STRING COMMA STRING RPAREN'''
    value = "\"%s\".split(\"%s\")" % (p[3], p[5])
    p[0] = Node("split", None, value)

def p_split_id(p):
    '''split_id : SPLIT LPAREN ID COMMA STRING RPAREN'''
    value = "%s.split(\"%s\")" % (p[3], p[5])
    p[0] = Node("split", None, value)

#STRIP
def p_strip(p):
    '''strip : strip_str
             | strip_id'''
    p[0] = Node("strip", [p[1]])

def p_strip_str(p):
    '''strip_str : STRIP LPAREN STRING COMMA STRING RPAREN
                 | STRIP LPAREN STRING RPAREN'''
    if len(p) == 7:
        value = "\"%s\".strip(\'%s\')" % (p[3], p[5])
        p[0] = Node("strip", None, value)
    if len(p) == 5:
        value = "\"%s\".strip( )" % p[3]
        p[0] = Node("strip", None, value)

def p_strip_id(p):
    '''strip_id : STRIP LPAREN ID COMMA STRING RPAREN
                | STRIP LPAREN ID COMMA RPAREN'''
    if len(p) == 7:
        value = "%s.strip(\'%s\')" % (p[3], p[5])
        p[0] = Node("strip", None, value)
    if len(p) == 6:
        value = "%s.strip( )" % p[3]
        p[0] = Node("strip", None, value)

#STR
def p_str(p):
    '''str : str_num
           | str_id'''
    p[0] = Node("str", [p[1]])

def p_str_num(p):
    '''str_num : STR LPAREN NUMBER RPAREN'''
    value = "str(%s)" % p[3]
    p[0] = Node("str", None, value)

def p_str_id(p):
    '''str_id : STR LPAREN ID RPAREN'''
    value = "str(%s)" % p[3]
    p[0] = Node("str", None, value)
