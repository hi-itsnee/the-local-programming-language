# Filename:                local.py
# Author:                  Team 13
# Description:             The local programming language compiler
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-05-02 16:33:12 plt>

import sys,os
import argparse
from localparse import parse
from localast import walk_the_tree
basepath = os.getcwd()+os.path.sep
sys.path.append(basepath+'libs')
sys.path.append(basepath+'statements')
sys.path.append(basepath+'functions')

def _output_code(code):
    '''Return string, which is target Python program'''
    # Initialize variables
    import_convertdist = False
    import_dist = False
    import_sys = False
    # Determine if we need to import anything
    if "convertdist(" in code:
        import_convertdist = True
    if " dist(" in code:
        import_dist = True
    if "argv[" in code:
        import_sys = True
    # Split on newlines, then we'll remove emtpy lines
    code = code.split("\n")
    # One can go insane making newlines/empty lines perfect throughout the
    # compiler, or they can be stripped out here
    clean_code = [ ]
    clean_code.append("import sys,os")
    clean_code.append("basepath=os.getcwd()+os.path.sep")
    clean_code.append(r"sys.path.append(basepath+'libs')")
    clean_code.append(r"sys.path.append(basepath+'functions')")
    clean_code.append(r"sys.path.append(basepath+'statements')")
    if import_convertdist:
        clean_code.append("from conversion import convertdist")
    if import_dist:
        clean_code.append("from haversine import dist")
    for line in code:
        if not line.strip():
            # Blank line
            continue
        else:
            clean_code.append(line)
    # Print file sans empty lines
    return "\n".join(clean_code)

def main(filename, debug, parse_only):
    '''Main function of local compliler'''
    # Read the source file and build the AST
    sourcecode = filename.read()
    ast = parse(sourcecode, debug)
    if parse_only:
        exit(0)
    if not ast:
        print "Error compiling"
        exit(1)
    # Walk the AST to produce target (Python) code
    target_code = walk_the_tree(ast, debug=debug)
    
    testfile_oldpath = str(sys.argv[1])
    
    position_of_extention = testfile_oldpath.index(".")
    
    testfile_newpath = testfile_oldpath[0:position_of_extention+1] + "py"
    
    try:
        writetofile = open(testfile_newpath, "w")
        output_code = _output_code(target_code) + "\n"
        writetofile.write(output_code)
    
        writetofile.close()
        print "File written successfully to " + testfile_newpath
    except Exception:
        print "Cannot generate code or write to file"
        exit(1)

def tester(testinput):
    '''Driver function to be used by test suite'''
    ast_test = parse(testinput)
    code = walk_the_tree(ast_test)
    return _output_code(code)

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
