import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

point_vals = {'(':1,'[':2,'{':3,'<':4}
pairs = {'(':')','[':']','{':'}','<':'>'}

scores = []

for line in data:
    char_stack = []
    is_corrupted = False
    for char in line:
        if char in pairs.keys():
            char_stack.append(char)
        elif char == pairs[char_stack[-1]]:
            char_stack = char_stack[:-1]
        else:
            is_corrupted = True
            break
    if is_corrupted:
        continue

    points = 0
    for char in char_stack[::-1]:
        points = (points * 5) + point_vals[char]
    scores.append(points)

middle_score_ix = int((len(scores)-1) / 2)
print(sorted(scores)[middle_score_ix])
