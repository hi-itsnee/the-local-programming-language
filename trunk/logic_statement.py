# Filename:		logic_statement.py
# Author:               Team 13
# Description:          local parser logic statements
# Supported Language(s):Python 2.x

from localast import Node

def p_logic_statement(p):
    '''logic_statement : ID EQUALS logic_expr SEMI'''

    value = "%s = " % (p[1]) 
    p[0] = Node("logic_statement",[p[3]], value, None)

def p_logic_expr(p):
    '''logic_expr : and_statement
		  | or_statement
                  | not_statement
                  | end_statement'''

    p[0] = Node("logic_expr",[p[1]],None,None)

def p_end_statement(p):
    '''end_statement : ID '''

    value = "%s" % (p[1])
    p[0] = Node("end_statement",None, value, value)

# AND
def p_and_statement(p):
    '''and_statement : ID AND logic_expr '''
    value = "%s and " % (p[1])
    p[0] = Node("and", [p[3]], value , None) 

#OR
def p_or_statement(p):
    '''or_statement : ID OR logic_expr '''
    value = "%s or " % (p[1])
    p[0] = Node("or", [p[3]], value, None)

#NOT
def p_not_statement(p):
    '''not_statement : NOT logic_expr '''

    p[0] = Node("not", [p[2]], "not", None)  
