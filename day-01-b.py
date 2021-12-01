import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [int(line) for line in data]

#data = [199,200,208,210,200,207,240,269,260,263]

num_larger = 0
for i in range(len(data)-3):
    diff = data[i+3] - data[i]
    if diff > 0:
        num_larger += 1
print(num_larger)
