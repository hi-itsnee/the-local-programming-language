##### Expected output .py files for comparison

### PROGRAM TESTS:
# Hello World:
helloworld_test = '''print "Hello, world!"'''

# example1.py python outputs:
example1_test = '''x = 1
y = 2
z = 1.1
w1 = x + y
w2 = x - y
w3 = x + z'''
    # I'm not following the output of this at all...

# Tutorial2 test:
tutorial2_test = '''from haversine import dist
c1 = (40.730836, -73.99749)
c2 = (40.808596, -73.961527)
d = dist(c1, c2)
print "The distance between %s and %s is %s meters" % (c1, c2, d)'''

# Tutorial3 test:
tutorial3_test = '''from haversine import dist
me = (1.0, 2.0)
coords = [(3.0, 4.0), (5.0, 6.0), (7.0, 8.0)]
shortest = 0
for coord in coords:
    d = dist(me, coord)
    if ((d < shortest) or (shortest == 0)):
        shortest = d
        closest = coord'''
    # Why does it get rid of the me = (1, 2) line?
    # What is the syntax error at line 9 near , ? 

# Tutorial4 test:
tutorial4_test = '''from haversine import dist
me = (40.752662, -73.977073)
radius = 500
try:
    places = open("database.csv", "r")
except Exception:
    print "Cannot open file"
    exit(1)
for place in places:
    coord, name, type = place.split(";")
    type = type.strip()
    if type != "pizza":
        continue
    d = dist(me, coord)
    if d <= radius:
        name = name.strip()
        print "%s is near me." % (name)'''

# Tutorial5 test:
tutorial5_test = '''print "You don't have enough time."'''
    # Syntax errors but it passes?

