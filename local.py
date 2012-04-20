# Filename:                local.py
# Author:                  Team 13
# Description:             The local programming language compiler
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-20 12:48:47 plt>

import argparse
from localparse import parse
from localast import walk_the_tree

def main(filename, debug, parse_only):
    # Read the source file and build the AST
    sourcecode = filename.read()
    ast = parse(sourcecode, debug)
    if parse_only:
        exit(0)
    if not ast:
        print "Error compiling"
        exit(1)
    # Walk the AST to produce target (Python) code
    code = walk_the_tree(ast, debug=debug).split("\n")
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

def tester(testinput):
    ast_test = parse(testinput)
    code = walk_the_tree(ast_test).split("\n")
    clean_code = [ ]
    for line in code:
        if not line.strip():
            continue
        else:
            clean_code.append(line)
    return "\n".join(clean_code)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='The local compiler.')
    argparser.add_argument('filename', metavar='FILENAME',
                           type=argparse.FileType('r'),
                           help='The local sourcecode')
    argparser.add_argument('-d', '--debug', action='store_true', dest='debug',
                           default=False,
                           help='Enable debugging (default: false)')
    argparser.add_argument('-p', '--parse', action='store_true', dest='parse',
                           default=False,
                           help='Exit after parsing (default: false)')
    try:
        args = argparser.parse_args()
        main(args.filename, args.debug, args.parse)
    except Exception as e:
        argparser.error(str(e))
