# Filename:                locallex.py
# Author:                  Team 13
# Description:             The local programming language lexer
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-05 20:20:34 plt>

import ply.lex as lex
import re

# Enable/disable debugging
DEBUG = False

reserved = (
    'PRINT', 'OPEN', 'CLOSE', 'IF', 'ELIF', 'ELSE', 'AND', 'OR', 'NOT',
    'WHILE', 'EXIT', 'APPEND', 'REMOVE', 'POP', 'DEF', 'PASS', 'FOR', 'IN',
    'CONTINUE', 'BREAK', 'RETURN', 'TRY', 'EXCEPT', 'DIST', 'CONVERTDIST',
    'LEN', 'STRIP', 'SPLIT', 'STR', 'READ', 'ARGV', 'NUM', 'JOIN'
    )

tokens = reserved + (
    # Operators and assignment
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'MODULO',
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'PLUSPLUS', 'MINUSMINUS', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    # Delimeters
    'SEMI', 'LPAREN', 'RPAREN', 'COMMA', 'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',

    # Literals ('list' is in parser, not lexer)
    'ID', 'COORD', 'STRING', 'NUMBER', 'BOOL', 'NULL',
    )

# Ignore whitespace
t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COORD(t):
    r'\(\s*[+-]?\d+(\.\d*)?\s*,\s*[+-]?\d+(\.\d*)?\s*\)'
    #split the string into two parts - lat and long - and make that a tuple
    m = str(t.value)
    pattern = '(?P<lat>[+-]?\d+(\.\d*)?)\s*,\s*(?P<longi>[+-]?\d+(\.\d*)?)'
    mo = re.search(pattern, m)
    lat = mo.group('lat')
    longi = mo.group('longi')
    # COORD can be a coordinte, or a two-number arg_list.  Make sure to
    # preserve programmer intentions
    if '.' in lat:
        lat = float(lat)
    else:
        lat = int(lat)
    if '.' in longi:
        longi = float(longi)
    else:
        longi = int(longi)
    mw = ( )
    mw += (lat,)
    mw += (longi,)
    t.value = str(mw)
    return t

def t_NUMBER(t):
    r'(\d+(\.\d*)?|\.\d+)([eE][-+]? \d+)?'
    return t

def t_BOOL(t):
   r'true|false'
   if t.value == "true":
       t.value = "True"
   elif t.value == "false":
       t.value = "False"
   return t

def t_NULL(t):
   r'null'
   t.value = "None"
   return t

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
t_LT               = r'<'
t_LE               = r'<='
t_GT               = r'>'
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='

# Assignment operators
t_EQUALS           = r'='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_MODEQUAL         = r'%='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='

# Increment/decrement
t_PLUSPLUS         = r'\+\+'
t_MINUSMINUS       = r'--'

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_COMMA            = r','
t_SEMI             = r';'

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
    #t.value = t.value[1:-1].decode("string-escape")
    return t

# Comments
def t_comment(t):
    r"\'\'\'(.|\n)*?\'\'\'|//(.)*?\n"
    t.lexer.lineno += t.value.count("\n")

# Lexical errors
def t_error(t):
    print("Illegal character %s at line %d" %
          (repr(t.value[0]), t.lexer.lineno))
    t.lexer.skip(1)

lexer = lex.lex(debug=DEBUG)

if __name__ == "__main__":
    lex.runmain(lexer)
