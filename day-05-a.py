import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [line.split(' -> ') for line in data]
data = [[line[0].split(','),line[1].split(',')] for line in data]
data = [[list(map(int,line[0])), list(map(int,line[1]))] for line in data]

field_size = 1000
field = [ [0 for x in range(field_size)] for y in range(field_size) ]
for p1,p2 in data:
    if p1[0]==p2[0]:
        x = p1[0]
        y1 = min(p1[1],p2[1])
        y2 = max(p1[1],p2[1])
        for y in range(y1,y2+1):
            field[x][y] += 1
    elif p1[1]==p2[1]:
        y = p1[1]
        x1 = min(p1[0],p2[0])
        x2 = max(p1[0],p2[0])
        for x in range(x1,x2+1):
            field[x][y] += 1

num_overlaps = 0
for row in field:
    for value in row:
        if value>1:
            num_overlaps += 1
print(num_overlaps)
