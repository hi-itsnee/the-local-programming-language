# Filename:                cond_statement.py
# Author:                  Team 13
# Description:             local language parser conditional statements
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-05-05 14:43:37 plt>

from local.localast import Node  # Node(type, children=None, value=None, line=None)


def p_cond_stmt(p):
    """cond_stmt : if_stmt %prec IFX
                 | elif_stmt %prec ELIF
                 | elif_else_stmt %prec ELIF
                 | if_else_stmt %prec ELSE"""
    p[0] = Node("cond_stmt", [p[1]])


# IF
def p_if_stmt(p):
    """if_stmt : if_simple
               | if_brace"""
    p[0] = Node("if_stmt", [p[1]])


def p_if_simple(p):
    """if_simple : IF expr stmt"""
    p[0] = Node("if", [p[2], p[3]])


def p_if_brace(p):
    """if_brace : IF expr LBRACE stmt_list RBRACE"""
    p[0] = Node("if", [p[2], p[4]])


# ELIF
def p_elif_stmt(p):
    """elif_stmt : elif_simple
                 | elif_brace"""
    p[0] = Node("elif_stmt", [p[1]])


def p_elif_simple(p):
    """elif_simple : IF expr stmt elif_block"""
    p[0] = Node("elif", [p[2], p[3], p[4]])


def p_elif_brace(p):
    """elif_brace : IF expr LBRACE stmt_list RBRACE elif_block"""
    p[0] = Node("elif", [p[2], p[4], p[6]])


def p_elif_block(p):
    """elif_block : elif_block ELIF expr LBRACE stmt_list RBRACE
                  | ELIF expr LBRACE stmt_list RBRACE
                  | elif_block ELIF expr stmt
                  | ELIF expr stmt"""
    if len(p) == 7:
        p[0] = Node("elif_block_brace", [p[1], p[3], p[5]])
    if len(p) == 6:
        p[0] = Node("elif_block_brace", [p[2], p[4]])
    if len(p) == 5:
        p[0] = Node("elif_block_simple", [p[1], p[3], p[4]])
    if len(p) == 4:
        p[0] = Node("elif_block_simple", [p[2], p[3]])


# ELIF/ELSE
def p_elif_else_stmt(p):
    """elif_else_stmt : elif_else_simple
                      | elif_brace_else
                      | elif_else_brace
                      | elifelse_braces"""
    p[0] = Node("elif_else_stmt", [p[1]])


def p_elif_else_simple(p):
    """elif_else_simple : IF expr stmt elif_block ELSE stmt"""
    p[0] = Node("elif_else", [p[2], p[3], p[4], p[6]])


def p_elif_brace_else(p):
    """elif_brace_else : IF expr LBRACE stmt_list RBRACE elif_block ELSE stmt"""
    p[0] = Node("elif_else", [p[2], p[4], p[6], p[8]])


def p_elif_else_brace(p):
    """elif_else_brace : IF expr stmt elif_block ELSE LBRACE stmt_list RBRACE"""
    p[0] = Node("elif_else", [p[2], p[3], p[4], p[7]])


def p_elifelse_braces(p):
    """elifelse_braces : IF expr LBRACE stmt_list RBRACE elif_block ELSE LBRACE stmt_list RBRACE"""
    p[0] = Node("elif_else", [p[2], p[4], p[6], p[9]])


# ELSE
def p_if_else_stmt(p):
    """if_else_stmt : if_else_simple
                    | if_brace_else
                    | if_else_brace
                    | ifelse_braces"""
    p[0] = Node("if_else_stmt", [p[1]])


def p_if_else_simple(p):
    """if_else_simple : IF expr stmt ELSE stmt"""
    p[0] = Node("else", [p[2], p[3], p[5]])


def p_if_brace_else(p):
    """if_brace_else : IF expr LBRACE stmt_list RBRACE ELSE stmt"""
    p[0] = Node("else", [p[2], p[4], p[7]])


def p_if_else_brace(p):
    """if_else_brace : IF expr stmt ELSE LBRACE stmt_list RBRACE"""
    p[0] = Node("else", [p[2], p[3], p[6]])


def p_ifelse_braces(p):
    """ifelse_braces : IF expr RBRACE stmt_list RBRACE ELSE LBRACE stmt_list"""
    p[0] = Node("else", [p[2], p[4], p[8]])
