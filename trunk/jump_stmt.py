# Filename:                jump_stmt.py
# Author:                  Team 13
# Description:             local parser jump statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-24 12:56:01 plt>

from localast import Node

def p_jump_stmt(p):
    '''jump_stmt : cont_jump_stmt
                 | break_jump_stmt
                 | pass_jump_stmt
                 | return_jump_stmt'''
    p[0] = Node("jump", [p[1]])

def p_cont_jump_stmt(p):
    '''cont_jump_stmt : CONTINUE'''
    value = "continue"
    p[0] = Node("continue", None, value, value)

def p_break_jump_stmt(p):
    '''break_jump_stmt : BREAK'''
    value = "break"
    p[0] = Node("break", None, value, value)

def p_pass_jump_stmt(p):
    '''pass_jump_stmt : PASS'''
    value = "pass"
    p[0] = Node("pass", None, value, value)

def p_return_jump_stmt(p):
    '''return_jump_stmt : RETURN expr
                        | RETURN'''
    if len(p) == 3:
        p[0] = Node("return", [p[2]], None, "return %s")
    elif len(p) == 2:
       p[0] = Node("return", None, "return")
