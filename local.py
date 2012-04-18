# Filename:                local.py
# Author:                  Team 13
# Description:             The local programming language compiler
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-18 10:51:32 plt>

import sys
from localparse import parse
from localast import walk_the_tree

# Enable debugging
DEBUG = True

# Parse the input. There should be one argument: the program to compile.
if len(sys.argv) == 2:
    sourcecode = open(sys.argv[1]).read()
    ast = parse(sourcecode, DEBUG)
    if not ast:
        raise SystemExit
else:
    print "Usage: python local.py PROGNAME"
    print "where PROGNAME = the program name"
    exit(1)

# Walk the AST to produce target (Python) code
code = walk_the_tree(ast, debug=DEBUG).split("\n")

# One can go insane making newlines/empty lines perfect throughout the
# compiler, or they can be stripped out here
clean_code = [ ]
for line in code:
    if not line.strip():
        # Blank line
        continue
    else:
        clean_code.append(line)
# Print file sans empty lines
print "\n".join(clean_code)
