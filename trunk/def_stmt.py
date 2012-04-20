# Filename:                except_statement.py
# Author:                  Team 13
# Description:             local language parser exception statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-20 14:41:57 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_def_stmt(p):
    '''def_stmt : DEF ID LPAREN atom RPAREN LBRACE stmt_list RBRACE
                | DEF ID LPAREN atom RPAREN LBRACE PASS SEMI RBRACE'''
