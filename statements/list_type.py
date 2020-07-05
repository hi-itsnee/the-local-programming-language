# Filename:                list_type.py
# Author:                  Team 13
# Description:             local list composite datatype
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-05-05 13:42:14 plt>

from localast import Node


def p_list(p):
    '''list : LBRACKET RBRACKET
            | LBRACKET list_body RBRACKET'''
    if len(p) == 3:
        p[0] = Node("list", None, "[]")
    elif len(p) == 4:
        p[0] = Node("list", [p[2]])


def p_list_body(p):
    '''list_body : list_body list_item
                 | list_item'''
    if len(p) == 2:
        p[0] = Node("list_body", [p[1]])
    elif len(p) == 3:
        p[0] = Node("list_body", [p[1], p[2]])


def p_list_item(p):
    '''list_item : single_item
                 | comma_item'''
    p[0] = Node("list_item", [p[1]])


def p_single_item(p):
    '''single_item : atom
                   | list'''
    p[0] = Node("single_item", [p[1]])


def p_comma_item(p):
    '''comma_item : COMMA atom
                  | COMMA list'''
    p[0] = Node("comma_item", [p[2]])
