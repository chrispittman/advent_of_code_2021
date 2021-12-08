import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [line.split(' | ') for line in data]
data = [[line[0].split(), line[1].split()] for line in data]

count = 0
for line in data:
     for val in line[1]:
          if len(val) in [2,4,3,7]:
              count += 1
print(count)
