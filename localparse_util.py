# Filename:                localparse_util.py
# Author:                  Team 13
# Description:             The local progamming language parser utilies
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-03-21 17:12:36 mc>

# Number of space a tab equals
INDENT = 4

# Send semantically equivalent Python code to stdout
emit_code = True

def print_code(code, indent):
    indent *= INDENT
    if not emit_code:
        return
    codelines = code.splitlines()
    for c in codelines:
        print "%s%s" % (" "*indent, c)
