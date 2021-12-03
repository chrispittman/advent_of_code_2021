import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

def most_common_value(data, posn):
    num_ones = 0
    for datum in data:
        if datum[posn] == '1':
            num_ones += 1
    return "1" if num_ones*2>=len(data) else "0"


rating1 = data[:]
rating1_posn = 0
while len(rating1)>1:
    mcv = most_common_value(rating1, rating1_posn)
    rating1 = list(filter(lambda x: x[rating1_posn]==mcv, rating1))
    rating1_posn += 1

rating2 = data[:]
rating2_posn = 0
while len(rating2)>1:
    mcv = most_common_value(rating2, rating2_posn)
    rating2 = list(filter(lambda x: x[rating2_posn]!=mcv, rating2))
    rating2_posn += 1

print (int(rating1[0], 2) * int(rating2[0], 2))
