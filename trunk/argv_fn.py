# Filename:                argv_fn.py
# Author:                  Team 13
# Description:             local parser argv function
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-05 13:44:51 plt>

from localast import Node

def p_argv_fn(p):
    '''argv_fn : ARGV list'''
    line = "sys.argv%s"
    p[0] = Node("argv", [p[2]], None, line)
