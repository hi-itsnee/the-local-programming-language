from localast import Node

def p_exit_statement(p):
	'''exit_statement : EXIT LPAREN NUMBER RPAREN SEMI'''
	
	line = "exit(%s)\n" % (p[3])
	p[0] = Node("exit", None, None, line)
