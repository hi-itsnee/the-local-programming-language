# Filename:                exit_stmt.py
# Author:                  Team 13
# Description:             local parser exit statement
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-04-24 12:52:48 plt>

from local.localast import Node  # Node(type, children=None, value=None, line=None)


def p_exit_stmt(p):
    """exit_stmt : EXIT LPAREN NUMBER RPAREN"""
    value = "exit(%s)\n" % (p[3])
    p[0] = Node("exit", None, value, None)
