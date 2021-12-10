import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

point_vals = {')':3,']':57,'}':1197,'>':25137}
pairs = {'(':')','[':']','{':'}','<':'>'}

points = 0

for line in data:
    char_stack = []
    for char in line:
        if char in pairs.keys():
            char_stack.append(char)
        elif char == pairs[char_stack[-1]]:
            char_stack = char_stack[:-1]
        else:
            points += point_vals[char]
            break

print (points)

