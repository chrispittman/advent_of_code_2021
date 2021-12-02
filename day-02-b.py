import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [line.split() for line in data]

[x,z,aim] = [0,0,0]

for [dir, dist_str] in data:
    dist = int(dist_str)
    if dir=='down':
        aim += dist
    if dir=='up':
        aim -= dist
    if dir=='forward':
        x += dist
        z += aim*dist
print(z, x, z*x)
