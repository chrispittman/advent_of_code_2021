import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

num_ones = [0] * len(data[0])
for posn in range(len(data[0])):
    for datum in data:
        if datum[posn] == '1':
            num_ones[posn] += 1

gamma = ""
epsilon = ""
for i in range(len(data[0])):
    if num_ones[i]*2 > len(data):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
gamma = int(gamma,2)
epsilon = int(epsilon,2)
print (gamma*epsilon)

