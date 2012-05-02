# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-05-02 17:32:17 plt>

from localast import Node

def p_assign_stmt(p):
    '''assign_stmt : id_list EQUALS expr
                   | math_assmnt'''
    if len(p) == 4:
        p[0] = Node("equals", [p[1],p[3]], None, "%s = %s")
    elif len(p) == 2:
        p[0] = Node("assign", [p[1]])
#    p[0] = Node("assign", [p[1], p[2], p[3]], None, "%s %s %s")

def p_id_list(p):
    '''id_list : id_list COMMA ID
               | ID'''
    if len(p) == 2:
        value = "%s" % (p[1])
        p[0] = Node("id", None, value, value)
    else:
        string = "%s" % (p[3])
        p[0] = Node("id_list", [p[1]], p[3], "%s,"+string)

def p_math_assmnt(p):
    '''math_assmnt : id_list TIMESEQUAL atom
                   | id_list DIVEQUAL atom
                   | id_list MODEQUAL atom
                   | id_list PLUSEQUAL atom
                   | id_list MINUSEQUAL atom
                   | id_list ANDEQUAL atom
                   | id_list OREQUAL atom'''
#    if p[0] = r'\*(\s)?=':
#        string = 
#    elif p[0] = r'/(\s)?='
#    if p[0] = r'%(\s)?='
#    if p[0] = r'\+(\s)?='
#    if p[0] = r'-(\s)?='
#    if p[0] = r'and(\s)?='
#    if p[0] = r'or(\s)?='
