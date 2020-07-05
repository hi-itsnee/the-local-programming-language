# Filename:                iter_stmt.py
# Author:                  Team 13
# Description:             local parser iteration statements
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-05-05 18:22:28 plt>

from local.localast import Node  # Node(type, children=None, value=None, line=None)


def p_iter_stmt(p):
    """iter_stmt : while_stmt
                 | for_stmt"""
    p[0] = Node("iter", [p[1]])


def p_while_stmt(p):
    """while_stmt : WHILE expr stmt
                  | WHILE expr LBRACE stmt_list RBRACE"""
    if len(p) == 4:
        p[0] = Node("while", [p[2], p[3]])
    elif len(p) == 6:
        p[0] = Node("while", [p[2], p[4]])


def p_for_stmt(p):
    """for_stmt : FOR ID IN atom stmt
                | FOR ID IN atom LBRACE stmt_list RBRACE"""
    if len(p) == 6:
        p[0] = Node("for", [p[4], p[5]], p[2])
    elif len(p) == 8:
        p[0] = Node("for", [p[4], p[6]], p[2])
