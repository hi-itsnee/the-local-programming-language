# Filename:                localast.py
# Author:                  Team 13
# Description:             local language AST utilities
# Supported Lanauge(s):    Python 2.x
# Time-stamp:              <2012-04-20 17:27:46 plt>

# Number of spaces a tab equals
INDENT = 4

# Indent your children if you are one of these statements
indent_them = ('if', 'elif', 'else', 'for', 'while', 'def', 'try', 'except', 'return')

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

def _def_subtree(node, code, debug):
    '''For indenting DEF code blocks'''
    def_arg = walk_the_tree(node.children[0], code, debug)
    def_stmt = walk_the_tree(node.children[1], code, debug).split("\n")
    def_stmt_i = ""
    for line in def_stmt:
        def_stmt_i += " "*INDENT + line + "\n"
    return "def %s (%s):\n%s\n" % (node.value, def_arg, def_stmt_i)

def _arglist_subtree(node, code, debug):
    if node.children:
        arg_child = "%s,%s" % (walk_the_tree(node.children[0], code, debug), node.value)
        return "%s" % arg_child

def _for_subtree(node, code, debug):
    '''For indenting For block'''
    for_atomchild = walk_the_tree(node.children[0], code, debug)
    for_stmtchild = walk_the_tree(node.children[1], code, debug).split("\n")
    for_stmt_indented = ""
    for line in for_stmtchild:
        for_stmt_indented += " "*INDENT + line + "\n"
    return "for %s in %s:\n%s" % (node.value, for_atomchild, for_stmt_indented)

def _while_subtree(node, code, debug):
    '''For indenting While loop block'''
    while_exprchild = walk_the_tree(node.children[0], code, debug)
    while_stmtchild = walk_the_tree(node.children[1], code, debug).split("\n")
    while_stmt_indented = ""
    for line in while_stmtchild:
        while_stmt_indented += " "*INDENT + line + "\n"
    return "while %s:\n%s" % (while_exprchild, while_stmt_indented)

def _return_subtree(node, code, debug):
    return_expr_child = walk_the_tree(node.children[0], code, debug)
    return "return %s" % (return_expr_child)    

def _except_subtree(node, code, debug):
    except_try_child = walk_the_tree(node.children[0], code, debug).split("\n")
    print node.children[1]
    except_catch_child = walk_the_tree(node.children[1], code, debug).split("\n")
    except_trychild_indented = ""
    except_catchchild_indented = ""

    for line in except_try_child:
        except_trychild_indented += " "*INDENT + line + "\n"
    for line in except_catch_child:
        except_catchchild_indented += " "*INDENT + line + "\n"
    print except_catch_child 
    return "try:\n%s\nexcept %s:\n%s" % (except_trychild_indented, node.value, except_catchchild_indented)

def _format_subtree(node, code, debug):
    format_print_statement_child = walk_the_tree(node.children[0], code, debug)
    return "%s %% (%s)" % (node.value, format_print_statement_child)

 
def _print_subtree(node, code, debug):
    if node.children:
        print_child = "%s,\"%s\"" % (walk_the_tree(node.children[0], code, debug), node.value)
    return "%s" % print_child


def _indent_subtree(node, code, debug):
    '''For indenting statements'''
    # IF
    if node.type == 'if':
        return _if_subtree(node, code, debug)
    # ELSE
    if node.type == 'else':
        return _else_subtree(node, code, debug)
    # DEF
    if node.type == 'def':
        return _def_subtree(node, code, debug)
    # Arguments of DEF
    if node.type == 'arglist':
        return _arglist_subtree(node, code, debug)
    # FOR
    if node.type == 'for':
        return _for_subtree(node, code, debug)
    # WHILE
    if node.type == 'while':
        return _while_subtree(node, code, debug)
    # RETURN
    if node.type == 'return':
        return _return_subtree(node, code, debug)
    # EXCEPT
    if node.type == 'except':
        return _except_subtree(node, code, debug)      

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
        elif node.type == "arglist":
            code += _indent_subtree(node, code, debug)
        elif node.type == "format_print_statement":
            code += _format_subtree(node, code, debug)
        elif node.type == "format_statement":
            code += _print_subtree(node, code, debug)
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
        if node.type == "format_statement":
            code = "\"" + node.value + "\""
        else:    
            code = node.value
    # Return statement for the function. Builds target code in order
    return code
