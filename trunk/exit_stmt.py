# Filename:                exit_stmt.py
# Author:                  Team 13
# Description:             local parser exit statement
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 12:52:48 plt>

from localast import Node

def p_exit_stmt(p):
    '''exit_stmt : EXIT LPAREN NUMBER RPAREN SEMI'''
    line = "exit(%s)\n" % (p[3])
    p[0] = Node("exit", None, line, line)
