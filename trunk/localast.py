# Filename:                localast.py
# Author:                  Team 13
# Description:             local language AST utilities
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-18 21:24:07 plt>

# Number of spaces a tab equals
INDENT = 4

# Indent your children if you are one of these statements
indent_them = ('if', 'elif', 'else', 'for', 'while', 'def', 'try', 'except')

# Node class for the AST
class Node:
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

def walk_the_tree(node, code="", debug=False):
    '''Walk the AST and return a string, which is a Python program'''
    # Default case (should not be hit)
    if node is None:
        return
    # Debugging to watch tree traversal
    if debug:
        print "#type: %s, value: %s" % (node.type, node.value)
    # Certain statements require substatements to be indented during the walk
    if node.type in indent_them:
        if node.type == 'if':
            # Walk tree to build expression
            expr = walk_the_tree(node.children[0], debug)
            # Walk tree to build statement and split statement on newlines
            if_stmt = walk_the_tree(node.children[1], debug).split("\n")
            if_stmt_i = ""
            # Add indents to all the lines in the statement
            for line in if_stmt:
                if_stmt_i += " "*INDENT + line + "\n"
            # Construct the if statment
            code += "if %s:\n%s" % (expr, if_stmt_i)
        if node.type == 'else':
            expr = walk_the_tree(node.children[0], debug)
            if_stmt = walk_the_tree(node.children[1], debug).split("\n")
            else_stmt = walk_the_tree(node.children[2], debug).split("\n")
            if_stmt_i = ""
            else_stmt_i = ""
            for line in if_stmt:
                if_stmt_i += " "*INDENT + line + "\n"
            for line in else_stmt:
                else_stmt_i += " "*INDENT + line + "\n"
            code += "if %s:\n%s\nelse:\n%s" % (expr, if_stmt_i, else_stmt_i)
    # If we need to synthesize a string, build a tuple from the subtree
    elif node.line:
        values = ( )
        # Visit the children
        for child in node.children:
            values = values + (walk_the_tree(child, code, debug),)
        code += (node.line % values)
    # Otherwise, just walk the tree
    else:
        for child in node.children:
            code = walk_the_tree(child, code, debug)
    # Set the return value
    if node.value:
        code = node.value
    # Return statement for the function. Builds target code in order
    return code
