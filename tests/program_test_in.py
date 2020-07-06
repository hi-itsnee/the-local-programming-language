##### Input .local files for testing

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

# Tutorial2 test:
tutorial2_test = '''c1 = (40.730836, -73.99749);
c2 = (40.808596, -73.961527);
d = dist(c1, c2);
print("The distance between %s and %s is %s meters", c1, c2, d);'''

# Tutorial3 test:
tutorial3_test = '''me = (1, 2);
coords = [(3, 4), (5, 6), (7, 8)];
shortest = 0;
for coord in coords {
    d = dist(me, coord);
    if ((d < shortest) or (shortest == 0)) {
        shortest = d;
        closest = coord;
    }
}'''

# Tutorial4 test:
tutorial4_test = '''me = (40.752662, -73.977073);
radius = 500;

try {
    places = open("database.csv");
} except Exception {
    print ("Cannot open file");
    exit(1);
}

for place in places {
    coord, name, type = split(place,";");
    type = strip(type);
    if type != "pizza"
        continue;
    d = dist(me, coord);
    if d <= radius {
        name = strip(name);
        print("%s is near me.", name);
    }
}'''

# Tutorial5 test:
tutorial5_test = '''walk_speed = 3.0;
def can_you_get_there(d, t) {
//Is the time necessary to cover the distance 
//faster than you can walk?  If yes, return false.
//If not, return true

    d_mi = convertdist(d, mi);
    trip_time = d_mi / (walk_speed * 60);

    if trip_time > t
        return false;
    else
        return true;
}

// Begin user prompts
print("Where are you starting? ");
start = read();
print("Where are you going? ");
stop = read();
print("How long do you have? ");
time = read();

try {
    d = dist(start, stop);
} except Exception {
    print ("Coordinate is not valid");
    exit(1);
}

try {
    if time < 0 {
        print("Time is not valid.");
        exit(1);
    }
} except Exception {
    print("Time is not valid.");
    exit(1);
}

if can_you_get_there(d, time)
    print("You can make it.");
else
    print("You don't have enough time.");'''
