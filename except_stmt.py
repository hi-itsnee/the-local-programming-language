# Filename:                except_stmt.py
# Author:                  Team 13
# Description:             local try/except statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 12:51:50 plt>

from localast import Node

def p_except_stmt(p):
    '''except_stmt : TRY LBRACE stmt_list RBRACE EXCEPT ID LBRACE stmt_list RBRACE'''
    p[0] = Node("except", [p[3], p[8]], p[6])
