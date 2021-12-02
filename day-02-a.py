import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [line.split() for line in data]

[x,z] = [0,0]

for [dir, dist_str] in data:
    dist = int(dist_str)
    if dir=='down':
        z += dist
    if dir=='up':
        z -= dist
    if dir=='forward':
        x += dist
print(z, x, z*x)
