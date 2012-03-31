# Filename:              assign_statement.py
# Author:                Team 13
# Description:           local parser assignment statements
# Supported Language(s): Python 2.x
# Time-stamp:            <2012-03-31 02:00:00>

from localparse_util import print_code

def p_assign_statement(p): 
    '''assign_statement : ID EQUALS ID 
                        | ID EQUALS NUMBER'''

    value = p[3]
    dest_var = p[1]
    dest_var = value
