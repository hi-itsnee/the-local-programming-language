# Filename:                localast.py
# Author:                  Team 13
# Description:             local language AST utilities
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-20 17:27:46 plt>

# Number of spaces a tab equals
INDENT = 4

# Indent your children if you are one of these statements
indent_them = ('if', 'elif', 'else', 'for', 'while', 'def', 'try', 'except')

# For variable declaration (this only works for global)
var_names = {}

class Node:
    '''Node class for the AST'''
    def __init__(self,
                 type,          # type of node
                 children=None, # children of the node
                 value=None,    # stored value of the node (a string)
                 line=None):    # Python line to by constructed from subtree
        self.type = type
        if children:
            self.children = children
        else:
            self.children = [ ]
        self.value = value
        self.line = line

def _if_subtree(node, code, debug):
    '''For indenting IF code blocks'''
    # Walk tree to build expression
    expr = walk_the_tree(node.children[0], code, debug)
    # Walk tree to build statement and split statement on newlines
    if_stmt = walk_the_tree(node.children[1], code, debug).split("\n")
    if_stmt_i = ""
    # Add indents to all the lines in the statement
    for line in if_stmt:
        if_stmt_i += " "*INDENT + line + "\n"
    # Construct the if statment
    return "if %s:\n%s" % (expr, if_stmt_i)

def _else_subtree(node, code, debug):
    '''For indenting IF/ELSE code blocks'''
    expr = walk_the_tree(node.children[0], code, debug)
    if_stmt = walk_the_tree(node.children[1], code, debug).split("\n")
    else_stmt = walk_the_tree(node.children[2], code, debug).split("\n")
    if_stmt_i = ""
    else_stmt_i = ""
    for line in if_stmt:
        if_stmt_i += " "*INDENT + line + "\n"
    for line in else_stmt:
        else_stmt_i += " "*INDENT + line + "\n"
    return "if %s:\n%s\nelse:\n%s" % (expr, if_stmt_i, else_stmt_i)

def _indent_subtree(node, code, debug):
    '''For indenting statements'''
    # IF
    if node.type == 'if':
        return _if_subtree(node, code, debug)
    # ELSE
    if node.type == 'else':
        return _else_subtree(node, code, debug)

def walk_the_tree(node, code="", debug=False):
    '''Walk the AST and return a string, which is a Python program'''
    # Default case (should not be hit)
    if node is None:
        return
    # Debugging to watch tree traversal
    if debug:
        print "#type: %s, value: %s" % (node.type, node.value)
    # For nodes with children
    if node.children:
        # Certain statements require substatements to be indented
        if node.type in indent_them:
            code += _indent_subtree(node, code, debug)
        # Assignments needs their right side synthesized
        elif node.type == "assign":
            rhs = walk_the_tree(node.children[0], code, debug)
            assmnt = node.value + " = " + rhs + "\n"
            code += assmnt
        # If we need to synthesize a string, build a tuple from the subtree
        elif node.line:
            values = ( )
            # Visit the children
            for child in node.children:
                values += (walk_the_tree(child, code, debug),)
            line = (node.line % values)
            # We're building a line here, not appending to target code
            code = line
        # Otherwise, just walk the tree
        else:
            for child in node.children:
                code = walk_the_tree(child, code, debug)
    # Otherwise is a leaf node (must have a value)
    else:
        code = node.value
    # Return statement for the function. Builds target code in order
    return code
