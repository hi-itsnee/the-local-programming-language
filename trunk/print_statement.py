from localast import Node
#Node(type, children=Node, value=None, line=None)

def p_string_statement(p):
    '''string_statement : print_statement'''
    p[0] = Node("print0", [p[1]])

def p_print_statement(p):
    '''print_statement : simple_print_statement
                       | format_print_statement'''
    p[0] = Node("print1", [p[1]])

def p_simple_print_statement(p):
    '''simple_print_statement : PRINT LPAREN STRING RPAREN SEMI'''
    value = "print \"%s\"\n" % p[3]
    p[0] = Node("simpleprint", None, value)

def p_format_print_statement(p):
    '''format_print_statement : PRINT LPAREN STRING COMMA format_statement RPAREN SEMI'''
    value = "print \"%s\"" % p[3]
#    print "=====================" + line + "======="
    p[0] = Node("format_print_statement", [p[5]], value)

def p_format_statement(p):
    '''format_statement : format_statement COMMA STRING
                        | STRING'''
    if len(p) == 4:
        p[0] = Node("format_statement", [p[1]], p[3], None)
    if len(p) == 2:
        value = p[1]
        p[0] = Node("format_statement", None, value)




