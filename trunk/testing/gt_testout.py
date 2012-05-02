##### Expected output .py files for comparison

### LEXING/PARSING TESTS:

# assign_stmt.py python outputs:
assign_test = '''a = 10
b = (0 + 1)
c = a + b
x = 1
distance = 1000.0
name = "New York"'''
#c *= a
#d /= a
#e %= 2
#f += 4
#g -= 5
#h and= a
#i or= b

# cond_stmt.py python outputs:
if_test = '''a = 5
if a > 3:
    print "a > 3"'''

ifelse_test = '''a = True
if a:
    print "a is true"
else:
    print "a is false"'''

nesting_test = '''if a:
    print "a is true"
    if b == a:
        print "made it here"
    elif b < a:
        print "made it there"
    else:
        print "made it everywhere"
else:
    print "a is false"'''

# coord_fn.py python outputs:
coord_test = '''a = (4.0, -5.9)
b = (3.996, -6.445)'''

# def_stmt.py python outputs:
def_test = '''def newfunction(argin):
    a = argin
    b = "rats"'''

# except_stmt.py python outputs:
except_test = '''try:
    a = (10.0, 5.25)
except Exception:
    print "oops!"
try:
    a = 5
except Exception:
    print "sigh"'''

# exit_stmt.py python output:
exit_test = '''exit(1)'''

# expr.py python outputs:
binop_test = '''a = 1 + 1
b = 2 - 2
c = 3 * 3
d = 4 / 4
e = 5 % 2
f = 6 ** 2
r = a or b
s = c and d
t = e < f
u = a <= b
v = c > d
w = e >= f
x = a == b
y = c != d
z = (e)'''

indices_test = '''b = a[c]'''

unary_test = '''a = 3 + 1
a = True
b = not a
c = -5
d = c + 1
e = c - 1'''

# io_stmt.py python outputs:
io_test = '''a = open("hello.local", "w")'''

# iter_stmt.py python outputs:
iter_test = '''a = open("hello.local", "w")'''

# jump_stmt.py python outputs:
jump_test = '''a = open("hello.local", "w")'''

# list_stmt.py python outputs:
list_test = '''a = open("hello.local", "w")'''

# math_expr.py python outputs:
math_test = '''a = isd + dsa * 12 + (7 / 5)'''

# print_stmt.py python outputs:
print_test = '''a = open("hello.local", "w")'''

# str_fn.py python outputs:
strfn_test = '''   '''
