#type: program, value: None
#type: stmt_list, value: None
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: walk_speed
#type: molecule, value: None
#type: atom, value: 3.0
#type: stmt, value: None
#type: def, value: None
#type: atom, value: d
#type: atom, value: tot_t
#type: atom, value: make_t
#type: stmt_list, value: None
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: transit_time
#type: divide, value: None
#type: molecule, value: None
#type: atom, value: d
#type: parens, value: None
#type: times, value: None
#type: molecule, value: None
#type: atom, value: walk_speed
#type: molecule, value: None
#type: atom, value: 60
#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "The time it will take you to get there is %s minutes"
#type: atom, value: transit_time
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: compare_time
#type: plus, value: None
#type: molecule, value: None
#type: atom, value: transit_time
#type: molecule, value: None
#type: atom, value: make_t
#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "The total time to travel and get coffee there is %s minutes"
#type: atom, value: compare_time
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: compare_time
#type: molecule, value: None
#type: num_fn, value: None
#type: num, value: None
#type: atom, value: compare_time
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: tot_t
#type: molecule, value: None
#type: num_fn, value: None
#type: num, value: None
#type: atom, value: tot_t
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: boo
#type: parens, value: None
#type: gt, value: None
#type: molecule, value: None
#type: atom, value: compare_time
#type: molecule, value: None
#type: atom, value: tot_t
#type: stmt, value: None
#type: cond_stmt, value: None
#type: if_else_stmt, value: None
#type: else, value: None
#type: parens, value: None
#type: molecule, value: None
#type: atom, value: boo
#type: stmt, value: None
#type: jump, value: None
#type: return, value: None
#type: molecule, value: None
#type: atom, value: False
#type: stmt, value: None
#type: jump, value: None
#type: return, value: None
#type: molecule, value: None
#type: atom, value: True
#type: stmt, value: None
#type: except, value: None
#type: stmt_list, value: None
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: places
#type: molecule, value: None
#type: io_fn, value: None
#type: open, value: None
#type: atom, value: "coffee.csv"
#type: stmt_list, value: None
#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "Cannot open file"
#type: stmt, value: None
#type: exit, value: exit(1)

#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "Where are you starting? "
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: start
#type: molecule, value: None
#type: io_fn, value: None
#type: read_stmt, value: raw_input()
#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "How long do you have until your next event? "
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: time
#type: molecule, value: None
#type: io_fn, value: None
#type: read_stmt, value: raw_input()
#type: stmt, value: None
#type: iter, value: None
#type: for, value: place
#type: atom, value: places
#type: stmt_list, value: None
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: name
#type: atom, value: coord
#type: atom, value: wait_t
#type: atom, value: make_t
#type: atom, value: URL
#type: molecule, value: None
#type: str_fn, value: None
#type: split, value: None
#type: atom, value: place
#type: atom, value: ";"
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: d
#type: molecule, value: None
#type: coord_fn, value: None
#type: dist, value: None
#type: atom, value: start
#type: atom, value: coord
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: d_mile
#type: molecule, value: None
#type: coord_fn, value: None
#type: convertdist, value: None
#type: atom, value: d
#type: atom, value: "mi"
#type: atom, value: "m"
#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "Distance between you and %s is %s miles"
#type: atom, value: name
#type: atom, value: d_mile
#type: stmt, value: None
#type: assign_stmt, value: =
#type: atom, value: time_at_shop
#type: plus, value: None
#type: molecule, value: None
#type: num_fn, value: None
#type: num, value: None
#type: atom, value: wait_t
#type: molecule, value: None
#type: num_fn, value: None
#type: num, value: None
#type: atom, value: make_t
#type: stmt, value: None
#type: except, value: None
#type: stmt_list, value: None
#type: stmt, value: None
#type: cond_stmt, value: None
#type: if_else_stmt, value: None
#type: else, value: None
#type: molecule, value: None
#type: def_fn, value: can_you_get_coffee
#type: atom, value: d
#type: atom, value: time
#type: atom, value: time_at_shop
#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "You have time to go to %s\n"
#type: atom, value: name
#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "You do not have time to go to %s\n"
#type: atom, value: name
#type: stmt_list, value: None
#type: stmt, value: None
#type: io_stmt, value: None
#type: print_stmt, value: None
#type: print, value: None
#type: atom, value: "Could not calculate time for %s\n"
#type: atom, value: name
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
    places = open("testing/coffee.csv", "r")
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
