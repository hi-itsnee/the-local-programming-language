# Filename:                localast.py
# Author:                  Team 13
# Description:             local language AST utilities
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-10 10:59:45 plt>

# Number of spaces a tab equals
INDENT = 4

# Indent your children if you are one of these statements
indent_them = ('if', 'elif', 'else', 'for', 'while', 'def', 'try', 'except')

# Do not indent expressions
no_indent = ('expr',)

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

# Function to walk the AST
def walk_the_tree(node, code="", indent=0, debug=False):
    # Default case (should not be hit)
    if node is None:
        return
    # Debugging to watch tree traversal
    if debug:
        print "#type: %s, value: %s" % (node.type, node.value)
    # If we need to synthesize a string, build a tuple from the subtree
    if node.line:
        values = ()
        # Ident our children if we're the start of a new block
        if node.type in indent_them:
            indent += INDENT
        for child in node.children:
            values = values + (walk_the_tree(child, code, indent, debug),)
        # Return to our level if we've indented our children
        if node.type in indent_them:
            indent -= INDENT
        code = code + " "*indent + (node.line % values)
    # Otherwise, just walk the tree
    else:
        for child in node.children:
            code = walk_the_tree(child, code, indent, debug)
    # Set the return value
    if node.value:
        if node.type in no_indent:
            indent = 0
        code = " "*indent + node.value
    # Return statement for the function. Builds target code in order
    return code
