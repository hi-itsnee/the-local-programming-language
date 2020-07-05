##### Input .local files for testing

### LEXING/PARSING TESTS:

# assign_stmt.py local test inputs:
assign_test = '''//Test variable assignment prior to initialization
a = b;'''

# cond_stmt.py local test inputs:
if_test = '''a = 3;
if a > 3
    print("a > 3");'''

ifelse_test = '''a = True;
if a
    print("a is true");
else
    print("a is false");'''

nesting_test = '''if a {
    print("a is true");
    if b == a
        print("made it here");
    elif b < a
        print("made it there");
    else
        print("made it everywhere");
}
else
    print("a is false");'''

# exit
exit_test = '''exit(1);'''

# expr.py python outputs:
binop_test = '''a = 1 + 1;
b = 2 - 2;
c = 3 * 3;
d = 4 / 4;
e = 5 % 2;
f = 6 ^ 2;
r = a or b;
s = c and d;
t = e < f;
u = a <= b;
v = c > d;
w = e >= f;
x = a == b;
y = c != d;
z = (e);'''

indices_test = '''b = a[c];'''

unary_test = '''a = 3++;
a = True;
b = not a;
c = -5;
d = c++;
e = c--;'''

# io_stmt.py local test inputs:
io_test = '''a = open("hello.local", "w");'''

# math_expr.py local test inputs:
math_test1 = '''a = isd + dsa * 12 + (7/5);'''

# str_fn.py local test inputs:
strfn_test = '''   '''

### PROGRAM TESTS:
# Hello World:
helloworld_test = '''print("Hello, world!");'''

# example1.py local test inputs:
example1_test = '''x = 1;
y = 2;
z = 1.1;
w1 = x + y;
w2 = x - y;
w3 = x + z;'''
