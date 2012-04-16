# Filename:                def_stmt.py
# Author:                  Team 13
# Description:             The local programming language parser
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-15 21:05:02 plt>

from list_funcn import *

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_def_stmt(p):
    '''def_stmt : list_funcn'''
    p[0] = Node("def_stmt", [p[1]])
