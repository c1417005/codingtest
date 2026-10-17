import math
import itertools

N = int(input())

coords = []
for _ in range(N):
    coords.append(tuple(map(int,input().split())))

ptns = list(itertools.permutations(list(range(N))))

dist_sum = 0
for ptn in ptns:
    for i in range(N-1):
        a = ptn[i]
        b = ptn[i+1]
        x1 = coords[a][0]
        y1 = coords[a][1]
        x2 = coords[b][0]
        y2 = coords[b][1]
        dist_sum += math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(dist_sum / len(ptns))



