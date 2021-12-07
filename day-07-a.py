import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [int(p) for p in data[0].split(',')]

#data = [16,1,2,0,4,2,7,1,2,14]

max_posn = max(data)
min_cost = None
min_cost_posn = None
for cand_p in range(max_posn+1):
     fuel_cost = 0
     for p in data:
         fuel_cost += abs(p-cand_p)
     if min_cost is None or fuel_cost<min_cost:
         min_cost = fuel_cost
         min_cost_posn = p
print(min_cost)
