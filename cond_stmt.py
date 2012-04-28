# Filename:                cond_statement.py
# Author:                  Team 13
# Description:             local language parser conditional statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-28 13:15:15 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_cond_stmt(p):
    '''cond_stmt : if_stmt %prec IFX
                 | elif_stmt %prec ELIF
                 | elif_else_stmt %prec ELIF
                 | if_else_stmt %prec ELSE'''
    p[0] = Node("cond_stmt", [p[1]])

# def p_cond_stmt(p):
#     '''cond_stmt : elif_stmt'''
#     p[0] = Node("cond_stmt", [p[1]])

# IF
def p_if_stmt(p):
    '''if_stmt : if_simple
               | if_brace'''
    p[0] = Node("if_stmt", [p[1]])

def p_if_simple(p):
    '''if_simple : IF expr stmt_list'''
    p[0] = Node("if", [p[2], p[3]])

def p_if_brace(p):
    '''if_brace : IF expr LBRACE stmt_list RBRACE'''
    p[0] = Node("if", [p[2], p[4]])

# ELIF
def p_elif_stmt(p):
    '''elif_stmt : elif_simple
                 | elif_brace'''

def p_elif_simple(p):
    '''elif_simple : IF expr stmt_list elif_block'''

def p_elif_brace(p):
    '''elif_brace : IF expr LBRACE stmt_list RBRACE elif_block'''

def p_elif_block(p):
    '''elif_block : elif_block_simple
                  | elif_block_brace'''

def p_elif_block_simple(p):
    '''elif_block_simple : elif_block ELIF expr stmt_list
                         | ELIF expr stmt_list'''

def p_elif_block_brace(p):
    '''elif_block_brace : elif_block ELIF expr LBRACE stmt_list RBRACE
                        | ELIF expr LBRACE stmt_list RBRACE'''

#ELIF/ELSE
def p_elif_else_stmt(p):
    '''elif_else_stmt : elif_else_simple
                      | elif_brace_else
                      | elif_else_brace
                      | elifelse_braces'''

def p_elif_else_simple(p):
    '''elif_else_simple : IF expr stmt_list elif_block ELSE stmt_list'''

def p_elif_brace_else(p):
    '''elif_brace_else : IF expr LBRACE stmt_list RBRACE elif_block ELSE stmt_list'''

def p_elif_else_brace(p):
    '''elif_else_brace : IF expr stmt_list elif_block ELSE LBRACE stmt_list RBRACE'''

def p_elifelse_braces(p):
    '''elifelse_braces : IF expr LBRACE stmt_list RBRACE elif_block ELSE LBRACE stmt_list RBRACE'''

# ELSE
def p_if_else_stmt(p):
    '''if_else_stmt : if_else_simple
                    | if_brace_else
                    | if_else_brace
                    | ifelse_braces'''
    p[0] = Node("if_else_stmt", [p[1]])

def p_if_else_simple(p):
    '''if_else_simple : IF expr stmt_list ELSE stmt_list'''
    p[0] = Node("else", [p[2], p[3], p[5]])

def p_if_brace_else(p):
    '''if_brace_else : IF expr LBRACE stmt_list RBRACE ELSE stmt_list'''
    p[0] = Node("else", [p[2], p[4], p[7]])

def p_if_else_brace(p):
    '''if_else_brace : IF expr stmt_list ELSE LBRACE stmt_list RBRACE'''
    p[0] = Node("else", [p[2], p[3], p[6]])

def p_ifelse_braces(p):
    '''ifelse_braces : IF expr RBRACE stmt_list RBRACE ELSE LBRACE stmt_list'''
    p[0] = Node("else", [p[2], p[4], p[8]])
