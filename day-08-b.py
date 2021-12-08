import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [line.split(' | ') for line in data]
data = [[line[0].split(), line[1].split()] for line in data]

sum = 0

for [signals,digits] in data:
    mapping = [None] * 10
    # map the ones with unique number of displays
    mapping[1] = [s for s in signals if len(s)==2][0]
    mapping[4] = [s for s in signals if len(s)==4][0]
    mapping[7] = [s for s in signals if len(s)==3][0]
    mapping[8] = [s for s in signals if len(s)==7][0]

    # gather the 5- and 6-length ones into lists
    len5 = [s for s in signals if len(s)==5]
    len6 = [s for s in signals if len(s)==6]

    # 3 is the only 5-length one with all the segments from 1
    mapping[3] = [s for s in len5 if mapping[1][0] in s and mapping[1][1] in s][0]
    len5.remove(mapping[3])
    # 6 is the only 6-length one without all the segments from 1
    mapping[6] = [s for s in len6 if (mapping[1][0] not in s or mapping[1][1] not in s)][0]
    len6.remove(mapping[6])

    # 'adg' are the ones shared between between all the remaining length-5 ones
    adg = [s for s in len5[0] if s in len5[1]]

    # 9 is the 6-length one with 'adg' in it
    mapping[9] = [s for s in len6 if adg[0] in s and adg[1] in s and adg[2] in s][0]
    # 0 is the other one
    mapping[0] = [s for s in len6 if s!=mapping[9]][0]

    # 'b' is the one that's in 4 but not in 3
    b = [s for s in mapping[4] if s not in mapping[3]][0]

    # 5 is the 5-length one with 'b' lit
    mapping[5] = [s for s in len5 if b in s][0]
    # 2 is the other one
    mapping[2] = [s for s in len5 if s!=mapping[5]][0]

    result = ''
    for d in digits:
        for i in range(10):
            if sorted(d)==sorted(mapping[i]):
                 result += str(i)
                 break
    sum += int(result)

print(sum)

