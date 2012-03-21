# Filename:                local.py
# Author:                  Team 13
# Description:             The local programming language compiler
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-03-20 22:28:05 mc>

import sys

# Account for Python 3.x
if sys.version_info[0] >= 3:
    print "Python 3.x is not supported, but we'll give it the old college try"
    raw_input = input

# The local parser
import localparse

# Parse the input. There should be one argument: the program to compile.
if len(sys.argv) == 2:
    data = open(sys.argv[1]).read()
    prog = localparse.parse(data)
    if not prog:
        raise SystemExit
else:
    print "Usage: python local.py PROGNAME"
    print "where PROGNAME = the program name"
    exit(1)
