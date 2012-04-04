# Filename:		logic_statement.py
# Author:               Team 13
# Description:          local parser logic statements
# Supported Language(s):Python 2.x

from localast import Node

def p_logic_statement(p):
    '''logic_statement : ID EQUALS logic_expr '''

    value = "%s = " % (p[1]) 
    p[0] = Node("logic_statement",[p[3]], value, None)

def p_logic_expr(p):
    '''logic_expr : and_or_statement
                  | not_statement
                  | end_statement '''

    p[0] = Node("logic_expr",[p[1]],None,None)

def p_end_statement(p):
    '''end_statement : ID SEMI'''

    value = "%s" % (p[1])
    p[0] = Node("end_statement",None, value, value)

def p_and_or_statement(p):
    '''and_or_statement : ID and_statement
			| ID or_statement'''

    value = "%s" % (p[1])
    p[0] = Node("and_or_statement",[p[2]],value,None)

# AND
def p_and_statement(p):
    '''and_statement : AND logic_expr '''

    p[0] = Node("and", [p[2]], "and" , None) 

#OR
def p_or_statement(p):
    '''or_statement : OR logic_expr '''
    
    p[0] = Node("or", [p[2]], "or", None)

#NOT
def p_not_statement(p):
    '''not_statement : NOT logic_expr '''

    p[0] = Node("not", [p[2]], "not", None)  
