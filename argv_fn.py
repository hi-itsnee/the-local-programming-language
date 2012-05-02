from localast import Node

def p_argv_fn(p):
    '''argv_fn : ARGV LIST'''
    s = p[2].strip('[]')
    s = s.strip('\'\'')
    value = "sys.argv[%s]" % s
    p[0] = Node("argv", None, value) 
