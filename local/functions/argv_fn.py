# Filename:                argv_fn.py
# Author:                  Team 13
# Description:             local parser argv function
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-05-05 13:44:51 plt>

from local.localast import Node  # Node(type, children=None, value=None, line=None)


def p_argv_fn(p):
    """argv_fn : ARGV list"""
    line = "sys.argv%s"
    p[0] = Node("argv", [p[2]], None, line)
