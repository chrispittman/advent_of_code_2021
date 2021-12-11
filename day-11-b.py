import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [[int(c) for c in line] for line in data]

grid_size = list(range(10))
def get_neighbors(x,y):
     ns = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
     return filter(lambda n: n[0] in grid_size and n[1] in grid_size , ns)

for step in range(10000):
    data = [[c+1 for c in line] for line in data]
    new_flash = True
    while new_flash:
        new_flash = False
        for x in range(len(data)):
            for y in range(len(data)):
                if data[x][y]>9:
                    new_flash = True
                    data[x][y]=0
                    for n in get_neighbors(x,y):
                        if data[n[0]][n[1]] != 0:
                            data[n[0]][n[1]] += 1
    dark = False
    for row in grid_size:
        for col in grid_size:
            if data[row][col]!=0:
                dark = True
    if not dark:
        break

print(step+1)
