# The local compiler - Team 13
# (based on Dave Beazley's BASIC)

import sys

# Account for Python 3.x
if sys.version_info[0] >= 3:
    print "Python 3.x is not supported, but we'll give it the old college try"
    raw_input = input

import localparse
#import localinterp

# If a filename has been specified, we try to run it.
# If a runtime error occurs, we bail out and enter interactive mode below.
if len(sys.argv) == 2:
    data = open(sys.argv[1]).read()
    prog = localparse.parse(data)
    if not prog:
        raise SystemExit
    # l = localinterp.localInterpreter(prog)
    # try:
    #     l.run()
    #     raise SystemExit
    # except RuntimeError:
    #     #pass
    #     exit(1)
else:
    print "Usage: python local.py PROGNAME"
    print "where PROGNAME = the program name"
    exit(1)


###############################################################################
# else:
#     b = localinterp.localInterpreter({})

# Interactive mode.  This incrementally adds/deletes statements
# from the program stored in the BasicInterpreter object.  In
# addition, special commands 'NEW','LIST',and 'RUN' are added.
# Specifying a line number with no code deletes that line from
# the program.

# while 1:
#     try:
#         line = raw_input("local> ")
#     except EOFError:
#         raise SystemExit
#     if not line: continue
#     line += "\n"
#     prog = localparse.parse(line)
#     if not prog:
#         continue
#     keys = list(prog)
#     if keys[0] > 0:
#          b.add_statements(prog)
#     else:
#          stat = prog[keys[0]]
#          if stat[0] == 'RUN':
#              try:
#                  b.run()
#              except RuntimeError:
#                  pass
#          elif stat[0] == 'LIST':
#              b.list()
#          elif stat[0] == 'BLANK':
#              b.del_line(stat[1])
#          elif stat[0] == 'NEW':
#              b.new()
