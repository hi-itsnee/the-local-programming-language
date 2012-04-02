# Filename:                localast.py
# Author:                  Team 13
# Description:             local language AST utilities
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-01 21:57:38 plt>

# Number of spaces a tab equals
INDENT = 4

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
def walk_the_tree(node, code="", debug=False):
    # Default case (should not be hit)
    if node is None:
        return
    # Debugging to watch tree traversal
    if debug:
        print "#type: %s, value: %s" % (node.type, node.value)
    # If we need to synthesis a string, build a tuple from subtree
    if node.line:
        values = ()
        for child in node.children:
            values = values + (walk_the_tree(child, code, debug),)
        code = code + (node.line % values)
    # Otherwise, just walk the tree
    else:
        for child in node.children:
            code = walk_the_tree(child, code, debug)
    # Append the node's value to the list
    if node.value:
        code = code + node.value
    # Return statement for the function. Builds target code in order
    return code
