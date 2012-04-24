from localast import Node

def p_def(p):
    '''def_stmt : DEF ID LPAREN arglist RPAREN LBRACE stmt_list RBRACE'''
    p[0] = Node("def", [p[4], p[7]], p[2])

def p_arglist(p):
    '''arglist : arglist COMMA ID
               | ID'''
    if len(p) !=2: 
        p[0] = Node("arglist", [p[1]], p[3])
    else:
        p[0] = Node("arglist", None, p[1])

