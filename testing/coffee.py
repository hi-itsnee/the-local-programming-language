from conversion import convertdist
from haversine import dist
walk_speed = 3.0
def can_you_get_coffee(d, tot_t, make_t):
    transit_time = d / (walk_speed * 60)
    print "The time it will take you to get there is %s minutes" % (transit_time)
    compare_time = transit_time + make_t
    print "The total time to travel and get coffee there is %s minutes" % (compare_time)
    compare_time = float(compare_time)
    tot_t = float(tot_t)
    boo = (compare_time > tot_t)
    if (boo):
        return False
    else:
        return True
try:
    places = open("coffee.csv", "r")
except Exception:
    print "Cannot open file"
    exit(1)
print "Where are you starting? "
start = raw_input()
print "How long do you have until your next event? "
time = raw_input()
for place in places:
    name, coord, wait_t, make_t, URL = place.split(";")
    d = dist(start, coord)
    d_mile = convertdist(d, "mi", "m")
    print "Distance between you and %s is %s miles" % (name, d_mile)
    time_at_shop = float(wait_t) + float(make_t)
    try:
        if can_you_get_coffee(d, time, time_at_shop):
            print "You have time to go to %s\n" % (name)
        else:
            print "You do not have time to go to %s\n" % (name)
    except Exception:
        print "Could not calculate time for %s\n" % (name)
