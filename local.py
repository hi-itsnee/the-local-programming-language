# Filename:                local.py
# Author:                  Team 13
# Description:             The local programming language compiler
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-05-02 16:33:12 plt>

"""The local language compiler."""

import argparse
import sys

import local
from local.localast import walk_the_tree
from local.localparse import parse


def main(filename, debug, parse_only):
    """Main function of the local compiler."""
    # Read the source file and build the AST
    sourcecode = filename.read()
    ast = parse(sourcecode, debug)
    if parse_only:
        exit(0)
    if not ast:
        print("Error compiling")
        exit(1)
    # Walk the AST to produce target (Python) code
    target_code = walk_the_tree(ast, debug=debug)

    testfile_oldpath = str(sys.argv[1])

    position_of_extention = testfile_oldpath.index(".")

    testfile_newpath = testfile_oldpath[0:position_of_extention + 1] + "py"

    try:
        writetofile = open(testfile_newpath, "w")
        output_code = local.output_code(target_code) + "\n"
        writetofile.write(output_code)

        writetofile.close()
        print("File written successfully to " + testfile_newpath)
    except Exception:  # noqa
        print("Cannot generate code or write to file")
        exit(1)


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
