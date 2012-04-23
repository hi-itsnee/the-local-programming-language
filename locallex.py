# Filename:                locallex.py
# Author:                  Team 13
# Description:             The local programming language lexer
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-20 16:57:28 plt>

import ply.lex as lex
import re as tre
#import decimal

# Enable/disable debugging
DEBUG = False

reserved = (
    'PRINT', 'OPEN', 'IF', 'ELSE', 'AND', 'OR', 'NOT',
    'EXIT', 'APPEND', 'REMOVE', 'POP', 'DEF', 'PASS',
    # 'ELIF','READ', 'FOR', 'IN', 'WHILE',
    # 'CONTINUE', 'BREAK', 'RETURN',
    # 'DIST',
    )

tokens = reserved + (
    # Operators and assignment
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'POWER', 'MODULO',
    # 'LT', 'LE', 'GT', 'GE', 'NE',

    # Delimeters
    'SEMI', 'LPAREN', 'RPAREN', 'COMMA', 'LBRACE', 'RBRACE',
    # 'PERIOD', 'LBRACKET', 'RBRACKET', 'DQUOTE',

    # Literals
    'ID','COORD', 'STRING', 'NUMBER', 'BOOL','NULL'
    )

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COORD(t):
   r'\([+-]?\d+\.\d+,[+-]?\d+\.\d+\)'
   #split the string into two parts - lat and long - and make that a list
   m = str(t.value)
   print m
   print "===================>"
   mo = tre.search('(?P<lat>[+-]?\d+\.\d+),(?P<longi>[+-]?\d+\.\d+)', m)
   mw = []
   mw.append( mo.group('lat'))
   mw.append( mo.group('longi'))
#  print mw
   #ms = str(m)
   #mw = list.append(tre.split('[+-]?\d+\.\d+', m, 2))
#   print t.type
#   t.type = tuple
#  print "boo"
#   print t.type
#   t.value = list([]) 
#   print t.value
   t.value = str(mw)
   return t

def t_NUMBER(t):
    r'(\d+(\.\d*)?|\.\d+)([eE][-+]? \d+)?'
    return t

def t_BOOL(t):
   r'true|false'
   return t

def t_NULL(t):
   r'null'
   return None

# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MODULO           = r'\%'
t_POWER            = r'\^'
t_OR               = r'or'
t_AND              = r'and'
t_NOT              = r'not'
# t_GT               = r'>'
# t_LE               = r'<='
# t_GE               = r'>='
# t_EQ               = r'=='
# t_NE               = r'!='

# Assignment operators
t_EQUALS           = r'='
# t_TIMESEQUAL       = r'\*='
# t_DIVEQUAL         = r'/='
# t_MODEQUAL         = r'%='
# t_PLUSEQUAL        = r'\+='
# t_MINUSEQUAL       = r'-='
# t_ANDEQUAL         = r'&='
# t_OREQUAL          = r'\|='
# t_XOREQUAL         = r'^='

# Increment/decrement
# t_PLUSPLUS         = r'\+\+'
# t_MINUSMINUS       = r'--'

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
# t_LBRACKET         = r'\['
# t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
# t_PERIOD           = r'\.'
t_SEMI             = r';'
#t_DQUOTE           = r'\"'

# Identifiers and reserved words
reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

# Variables
def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t

# Strings (double-quoted)
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value=t.value[1:-1].decode("string-escape")
    return t

# Comments
def t_comment(t):
    r"\'\'\'(.|\n)*?\'\'\'|//(.)*?\n"
    t.lexer.lineno += t.value.count("\n")

# Lexical errors
def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex(debug=DEBUG)

if __name__ == "__main__":
    lex.runmain(lexer)
