import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [int(line) for line in data[0].split(',')]

# fish = [3,4,3,1,2]
fish = data

for day in range(80):
    for i in range(len(fish)):
        if fish[i]==0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1

print(len(fish))
