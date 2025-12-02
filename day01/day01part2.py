lock_current = 50
zero = 0
with open("day01/data/lockinput") as datafile:
    for line in datafile:
        direction = line[0]
        distance = int(line[1:])
        zero += int(distance/100)
        distance = distance % 100
        if direction == "R":
            lock_new = lock_current + distance
            if lock_new >= 100:
                zero += 1
                lock_new -= 100
        if direction == "L":
            lock_new = lock_current - distance
            if lock_new < 0:
                if lock_current != 0:
                    zero += 1
                lock_new += 100
            if lock_new == 0:
                zero += 1
        lock_current = lock_new
print(zero)