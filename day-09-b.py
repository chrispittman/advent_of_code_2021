import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [[int(c) for c in line] for line in data]

def get_surround_posns(x,y,max_x,max_y):
    surrounds = []
    if x>0: surrounds.append([x-1,y])
    if y>0: surrounds.append([x,y-1])
    if x<max_x-1: surrounds.append([x+1,y])
    if y<max_y-1: surrounds.append([x,y+1])
    return surrounds

max_x = len(data)
max_y = len(data[0])
low_points = []
for x in range(max_x):
    for y in range(max_y):
        height = data[x][y]
        surrounds = []
        for [x1,y1] in get_surround_posns(x,y,max_x,max_y):
            surrounds.append(data[x1][y1])
        if height < min(surrounds):
            low_points.append([x,y])

# every low point defines a new basin.
# basins are bounded by '9's.
basins = []
for low_point in low_points:
    basin = [low_point]
    newfound_points = [low_point]
    while len(newfound_points) > 0:
        temp = []
        for p in newfound_points:
            surr = get_surround_posns(p[0],p[1],max_x,max_y)
            for s in surr:
                if data[s[0]][s[1]]==9:
                    continue
                if s not in basin:
                    temp.append(s)
                    basin.append(s)
        newfound_points = temp
    basins.append(basin)

sizes = sorted([len(b) for b in basins])
print(sizes[-1]*sizes[-2]*sizes[-3])
