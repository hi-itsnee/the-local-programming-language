# local parser
#

import ply.yacc as yacc
import locallex

emit_code = True

tokens = locallex.tokens

precedence = (
    # ('left', 'PLUS','MINUS'),
    # ('left', 'TIMES','DIVIDE'),
    # ('left', 'POWER'),
    # ('right','UMINUS')
    )

def p_program(p):
    '''program : program io_statement
               | io_statement'''

#### This catch-all rule is used for any catastrophic errors.  In this case,
#### we simply return nothing

def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1

def p_io_statement(p):
    '''io_statement : print_statement'''

def p_print_statement(p):
    '''print_statement : PRINT LPAREN STRING RPAREN SEMI'''
    code = "print \"%s\"" % p[3]
    print_code(code, 0)

#### Catastrophic error handler
def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")

lparser = yacc.yacc()

def parse(data, debug=1):
    lparser.error = 0
    p = lparser.parse(data, debug=debug)
    if lparser.error:
        return None
    return p

def print_code(code, indent):
    if not emit_code:
        return
    codelines = code.splitlines()
    for c in codelines:
        print "%s%s" % (" "*indent, c)
