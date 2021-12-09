import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [[int(c) for c in line] for line in data]

max_x = len(data)
max_y = len(data[0])
low_points = []
for x in range(max_x):
    for y in range(max_y):
        height = data[x][y]
        surrounds = []
        if x>0: surrounds.append(data[x-1][y])
        if y>0: surrounds.append(data[x][y-1])
        if x<max_x-1: surrounds.append(data[x+1][y])
        if y<max_y-1: surrounds.append(data[x][y+1])
        if height < min(surrounds):
            low_points.append(height)
print(sum(low_points) + len(low_points))
