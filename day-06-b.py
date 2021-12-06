import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [int(line) for line in data[0].split(',')]
fish = data

day_buckets = [0,0,0,0,0,0,0,0,0]
for f in fish:
     day_buckets[f] += 1

num_days = 256
for day in range(num_days):
    new_day_buckets = [0,0,0,0,0,0,0,0,0]
    new_fish = day_buckets[0]
    for i in [1,2,3,4,5,6,7,8]:
        new_day_buckets[i-1] = day_buckets[i]
    new_day_buckets[6] += new_fish
    new_day_buckets[8] = new_fish
    day_buckets = new_day_buckets

print(sum(day_buckets))
