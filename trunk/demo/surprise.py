from haversine import dist
coords = [(8, 4), (1, 6), (7, 3)]
coords2 = [(3, 2), (2, 9), (5, 7), (6, 4)]
shortest = 0
for coord in coords:
    for c2 in coords2:
        d = dist(coord, c2)
        if ((d < shortest) or (shortest == 0)):
            shortest = d
            closest = coord
            closest2 = c2
print "%s and %s are the closest pair." % (closest, closest2)