N = int(input())

S = list(map(int,input().split()))
T = list(map(int,input().split()))


ans = T[:]
for k in range(2 * N):
    i = k % N
    j = (i+1) % N
    ans[j] = min(ans[j] , ans[i] + S[i])

print("\n".join(map(str,ans)))