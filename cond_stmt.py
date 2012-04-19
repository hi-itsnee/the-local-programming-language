# Filename:                cond_statement.py
# Author:                  Team 13
# Description:             local language parser conditional statements
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-18 20:53:07 plt>

from localast import Node
# Node(type, children=None, value=None, line=None)

def p_cond_stmt(p):
    '''cond_stmt : if_stmt
                 | if_else_stmt'''
                      # | if_elif_statement
                      # | if_elif_else_statement
    p[0] = Node("cond_stmt", [p[1]])

# IF
def p_if_stmt(p):
    '''if_stmt : if_simple
               | if_lbrace'''
                    # | if_simple_parens
                    # | if_lbrace_parens'''
    p[0] = Node("if_stmt", [p[1]])

def p_if_simple(p):
    '''if_simple : IF expr stmt_list %prec IFX'''
    p[0] = Node("if", [p[2], p[3]])

def p_if_lbrace(p):
    '''if_lbrace : IF expr LBRACE stmt_list RBRACE %prec IFX'''
    p[0] = Node("if", [p[2], p[4]])

# def p_if_simple_parens(p):
#     '''if_simple_parens : IF LPAREN expression RPAREN statement_list'''
#     p[0] = Node("if", [p[3]], p[2], True, True)

# def p_if_lbrace_parens(p):
#     '''if_lbrace_parens : IF LPAREN expression RPAREN LBRACE statement_list'''
#     p[0] = Node("if", [p[4]], p[2], True, True)


# # ELIF
# def p_elif_statement(p):
#     '''elif_statement : elif_simple
#                       | elif_lbrace
#                       | elif_rbrace
#                       | elif_rlbrace
#                       | elif_simple_parens
#                       | elif_lbrace_parens
#                       | elif_rbrace_parens
#                       | elif_rlbrace_parens'''
#     p[0] = Node("elif_statement", [p[1]])

# def p_elif_simple(p):
#     '''elif_simple : ELIF expression statement_list'''
#     p[0] = Node("elif", [p[3]], p[2])

# def p_elif_lbrace(p):
#     '''elif_lbrace : ELIF expression LBRACE statement_list'''
#     p[0] = Node("elif", [p[4]], p[2])

# def p_elif_rbrace(p):
#     '''elif_rbrace : RBRACE ELIF expression statement_list'''
#     p[0] = Node("elif", [p[4]], p[3])

# def p_elif_rlbrace(p):
#     '''elif_rlbrace : RBRACE ELIF expression LBRACE statement_list'''
#     p[0] = Node("elif", [p[5]], p[3])

# def p_elif_simple_parens(p):
#     '''elif_simple_parens : ELIF LPAREN expression RPAREN statement_list'''
#     p[0] = Node("elif", [p[3], p[5]])

# def p_elif_lbrace_parens(p):
#     '''elif_lbrace_parens : ELIF LPAREN expression RPAREN LBRACE statement_list'''
#     p[0] = Node("elif", [p[4]], p[2])

# def p_elif_rbrace_parens(p):
#     '''elif_rbrace_parens : RBRACE ELIF LPAREN expression RPAREN statement_list'''
#     p[0] = Node("elif", [p[4]], p[3])

# def p_elif_rlbrace_parens(p):
#     '''elif_rlbrace_parens : RBRACE ELIF LPAREN expression RPAREN LBRACE statement_list'''
#     p[0] = Node("elif", [p[5]], p[3])


# ELSE
def p_if_else_stmt(p):
    '''if_else_stmt : if_else_simple
                    | if_else_lbrace'''
#                       | else_rbrace
#                       | else_rlbrace'''
    p[0] = Node("if_else_stmt", [p[1]])

def p_if_else_simple(p):
    '''if_else_simple : IF expr stmt_list ELSE stmt_list'''
    p[0] = Node("else", [p[2], p[3], p[5]])

def p_if_else_lbrace(p):
    '''if_else_lbrace : IF expr LBRACE stmt_list RBRACE ELSE stmt_list'''
    p[0] = Node("else", [p[2], p[4], p[7]])

# def p_else_rbrace(p):
#     '''else_rbrace : RBRACE ELSE statement_list'''
#     p[0] = Node("else", [p[3]])

# def p_else_rlbrace(p):
#     '''else_rlbrace : RBRACE ELSE LBRACE statement_list'''
#     p[0] = Node("else", [p[4]])
