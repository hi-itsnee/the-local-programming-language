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

# Tutorial2 test:
tutorial2_test = '''from haversine import dist
c1 = (40.730836, -73.99749)
c2 = (40.808596, -73.961527)
d = dist(c1, c2)
print "The distance between %s and %s is %s meters" % (c1, c2, d)'''

# Tutorial3 test:
tutorial3_test = '''from haversine import dist
me = (1, 2)
coords = [(3, 4), (5, 6), (7, 8)]
shortest = 0
for coord in coords:
    d = dist(me, coord)
    if ((d < shortest) or (shortest == 0)):
        shortest = d
        closest = coord'''

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
tutorial5_test = '''from conversion import convertdist
from haversine import dist
walk_speed = 3.0
def can_you_get_there(d, t):
    d_mi = convertdist(d, mi)
    trip_time = d_mi / (walk_speed * 60)
    if trip_time > t:
        return False
    else:
        return True
print "Where are you starting? "
start = raw_input()
print "Where are you going? "
stop = raw_input()
print "How long do you have? "
time = raw_input()
try:
    d = dist(start, stop)
except Exception:
    print "Coordinate is not valid"
    exit(1)
try:
    if time < 0:
        print "Time is not valid."
        exit(1)
except Exception:
    print "Time is not valid."
    exit(1)
if can_you_get_there(d, time):
    print "You can make it."
else:
    print "You don't have enough time."'''
