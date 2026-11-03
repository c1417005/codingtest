N,M = map(int,input().split())
a = sorted(map(int,input().split()))
b = sorted(map(int,input().split()))

i = j = 0
ans = float('inf')

while i < N and j < M:
    d = a[i]-b[j]
    if d == 0:
        # print(0)
        ans = 0
        break #break はループ後のprintも出てしまう。

    if d < 0:
        ans = min(ans,-d)
        i += 1
    else:
        ans = min(ans,d)
        j += 1

print(ans)