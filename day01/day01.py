def turn_dial(start, dir, dist):
    if dir == "R":
        next = start + dist
    else:
        next = start - dist
    return next

def at_zero(val):
    return val % 100 == 0

lock_current = 50
zero = 0
with open("day01/data/lockinput") as datafile:
    for line in datafile:
        lock_current = turn_dial(lock_current, line[0],int(line[1:]))
        if at_zero(lock_current):
            zero += 1

print(zero)