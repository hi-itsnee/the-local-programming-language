from localast import Node
from expr import *

def p_jump_stmt(p):
    '''jump_stmt : cont_jump_stmt
                 | break_jump_stmt
                 | pass_jump_stmt
                 | return_jump_stmt'''
    p[0] = Node("jump",[p[1]])

def p_cont_jump_stmt(p):
    '''cont_jump_stmt : CONTINUE SEMI'''
    value = "continue"  
    p[0] = Node("continue",None,value)

def p_break_jump_stmt(p):
    '''break_jump_stmt : BREAK SEMI'''
    value = "break"
    p[0] = Node("break",None,value)

def p_pass_jump_stmt(p):
    '''pass_jump_stmt : PASS SEMI'''
    value = "pass"
    p[0] = Node("pass",None,value)

def p_return_jump_stmt(p):
    '''return_jump_stmt : RETURN expr SEMI'''
    p[0] = Node("return",[p[2]])     


    
