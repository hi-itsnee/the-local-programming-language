from localast import Node

def p_except_stmt(p):
    '''except_stmt : TRY LBRACE stmt_list RBRACE EXCEPT ID LBRACE stmt_list RBRACE'''
   
    p[0] = Node("except",[p[3], p[8]],p[6])
