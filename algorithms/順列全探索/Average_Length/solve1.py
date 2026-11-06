import itertools
import math

N = int(input())

coords = []
for _ in range(N):
    coords.append(tuple(map(int,input().split())))

ptn = list(itertools.permutations(list(range(N))))

sum_dist = 0

for p in ptn:
    for i in range(N-1):
        a = p[i]
        b = p[i+1]
        x1 = coords[a][0]
        y1 = coords[a][1]
        x2 = coords[b][0]
        y2 = coords[b][1]
        sum_dist += math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(sum_dist/len(ptn))
