##### Expected output .py files for comparison

### DEMO TESTS:
coffee_test = '''walk_speed = 3.0
def can_you_get_coffee(d, tot_t, make_t):
    d_meters = convertdist(d, mi, m)
    transit_time = d_meters / (walk_speed * 60)
    compare_time = transit_time + make_t
    if compare_time > tot_t:
        return false
    else:
        return true
try:
    places = open("coffee.csv")
except Exception:
    print ("Cannot open file")
    exit(1)
print "Where are you starting? "
start = raw_input()
print "How long do you have until your next event? "
time = raw_input()

for place in places:
    name, coord, wait_t, make_t, URL = place.split(";")
    d = dist(start, coord)
    time_at_shop = wait_t + make_t
    try:
        if can_you_get_coffee(d, time, time_at_shop):
            print "You have time to go to %s" % (name)
        else:
            print "You do not have time to go to %s" % (name)
    except Exception:
        print "Could not calculate time for %s" % (name)'''
