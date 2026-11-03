N = int(input())

S = list(map(int,input().split()))
T = list(map(int,input().split()))

ans = T[:]
for k in range(2*N):
    i = k % N #余りの利用で円を表現できる。
    j = (i+1) % N
    T[j] = min(ans[i],T[i]+S[i])
