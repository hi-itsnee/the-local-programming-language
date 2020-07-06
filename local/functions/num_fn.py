# Filename:                num_fn.py
# Author:                  Team 13
# Description:             local parser number functions
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-05-05 17:59:19 plt>

from local.localast import Node  # Node(type, children=None, value=None, line=None)


def p_num_fn(p):
    """num_fn : num"""
    p[0] = Node("num_fn", [p[1]])


# NUM
def p_num(p):
    """num : NUM LPAREN atom RPAREN"""
    p[0] = Node("num", [p[3]], None, "float(%s)")
