# Filename:                except_stmt.py
# Author:                  Team 13
# Description:             local try/except statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-05 19:16:48 plt>

from localast import Node

def p_except_stmt(p):
    '''except_stmt : try_simple
                   | try_brace
                   | except_brace
                   | try_except_braces'''
    p[0] = Node("except", [p[1]])

def p_try_simple(p):
    '''try_simple : TRY stmt EXCEPT ID stmt'''
    p[0] = Node("try_simple", [p[2], p[5]], p[4])

def p_try_brace(p):
    '''try_brace : TRY LBRACE stmt_list RBRACE EXCEPT ID stmt'''
    p[0] = Node("try_brace", [p[3], p[7]], p[6])

def p_except_brace(p):
    '''except_brace : TRY stmt EXCEPT ID LBRACE stmt_list RBRACE'''
    p[0] = Node("except_brace", [p[2], p[6]], p[4])

def p_try_except_braces(p):
    '''try_except_braces : TRY LBRACE stmt_list RBRACE EXCEPT ID LBRACE stmt_list RBRACE'''
    p[0] = Node("try_except_braces", [p[3], p[8]], p[6])
