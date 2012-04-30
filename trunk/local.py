# Filename:                local.py
# Author:                  Team 13
# Description:             The local programming language compiler
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-29 23:22:45 plt>

import argparse
from localparse import parse
from localast import walk_the_tree

def main(filename, debug, parse_only):
    # Initialize variables
    import_convertdist = False
    import_dist = False
    import_sys = False
    # Read the source file and build the AST
    sourcecode = filename.read()
    ast = parse(sourcecode, debug)
    if parse_only:
        exit(0)
    if not ast:
        print "Error compiling"
        exit(1)
    # Walk the AST to produce target (Python) code
    code = walk_the_tree(ast, debug=debug)
    # Determine if we need to import anything
    if code.find("convertdist(") != -1:
        import_convertdist = True
    if code.find(" dist(") != -1:
        import_dist = True
    if code.find("argv[") != -1:
        import_sys = True
    # Split on newlines, then we'll remove emtpy lines
    code = code.split("\n")
    # One can go insane making newlines/empty lines perfect throughout the
    # compiler, or they can be stripped out here
    clean_code = [ ]
    if import_convertdist:
        clean_code.append("from conversion import convertdist")
    if import_dist:
        clean_code.append("from haversine import dist")
    if import_sys:
        clean_code.append("import sys")
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
