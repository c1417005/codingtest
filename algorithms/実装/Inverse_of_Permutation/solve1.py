N = int(input())
P = list(map(int,input().split()))
#pi 番目の要素がi

Q = [0]*N

for pi,p in enumerate(P):
    Q[p-1] = pi+1

print(*Q)
