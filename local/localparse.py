# Filename:                localparse.py
# Author:                  Team 13
# Description:             The local programming language parser
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-05-05 17:58:33 plt>

"""Local language parser."""

import ply.yacc as yacc
import local.locallex

from local.localast import Node  # Node(type, children=None, value=None, line=None)
from local.functions.argv_fn import *
from local.functions.coord_fn import *
from local.functions.list_fn import *
from local.functions.num_fn import *
from local.functions.str_fn import *

from local.statements.assign_stmt import *
from local.statements.cond_stmt import *
from local.statements.def_stmt import *
from local.statements.double_stmt import *
from local.statements.except_stmt import *
from local.statements.exit_stmt import *
from local.statements.expr import *
from local.statements.io_stmt import *
from local.statements.iter_stmt import *
from local.statements.jump_stmt import *
from local.statements.list_type import *
from local.statements.print_stmt import *
from local.statements.atom import *


# The tokens from our lexer
tokens = local.locallex.tokens

# The first rule
start = 'program'

# Operator precendence and associativity
precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELIF'),
    ('nonassoc', 'ELSE'),
    ('left', 'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('left', 'PLUSPLUS', 'MINUSMINUS'),
    ('left', 'POWER'),
    ('right', 'UMINUS')
)


def p_program(p):
    """program : program stmt_list
               | stmt_list"""
    if len(p) == 3:
        p[0] = Node("program", [p[1], p[2]])
    elif len(p) == 2:
        p[0] = Node("program", [p[1]])


def p_stmt_list(p):
    """stmt_list : stmt_list stmt
                 | stmt"""
    if len(p) == 3:
        p[0] = Node("stmt_list", [p[1], p[2]])
    elif len(p) == 2:
        p[0] = Node("stmt_list", [p[1]])


def p_stmt(p):
    """stmt : io_stmt SEMI
            | assign_stmt SEMI
            | cond_stmt
            | exit_stmt SEMI
            | def_stmt
            | iter_stmt
            | jump_stmt SEMI
            | list_fn SEMI
            | except_stmt
            | double_stmt SEMI"""
    p[0] = Node("stmt", [p[1]])


# Error handler
def p_error(p):  # noqa:pep257
    if not p:
        print("There is a catastrophic error in your code. I cannot help you.")
    else:
        print("Syntax error at line %s near %s" % (p.lineno, p.value))
        yacc.restart()


# The PLY parser (internally runs the lexer)
lparser = yacc.yacc()


def parse(data, debug=False):
    """Parse."""
    lparser.error = 0
    p = lparser.parse(data, debug=debug)  # The AST
    if lparser.error:
        return None
    return p
