from localast import Node

def p_exit_stmt(p):
	'''exit_stmt : EXIT LPAREN NUMBER RPAREN SEMI'''
	
	line = "exit(%s)\n" % (p[3])
	p[0] = Node("exit", None, None, line)
