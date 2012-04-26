# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-04-24 15:20:41 plt>

from localast import Node

def p_assign_stmt(p):
    '''assign_stmt : ID EQUALS expr SEMI'''
    p[0] = Node("assign", [p[3]],p[1])
#    p[0] = Node("assign", [p[1], p[2], p[3]])

def p_id_list(p):
    '''id_list : id_list COMMA ID
               | ID'''

def p_assmnt(p):
    '''assmnt : EQUALS
              | TIMESEQUAL
              | DIVEQUAL
              | MODEQUAL
              | PLUSEQUAL
              | MINUSEQUAL
              | ANDEQUAL
              | OREQUAL'''
