import bisect

d = int(input())
N = int(input())
M = int(input())

shop = [0]
home = []

for n in range(N-1):
    shop.append(int(input()))

for m in range(M):
    home.append(int(input()))

shop.sort()
shop.append(d) #0-dまで円を切って１列にするイメージ

ans = 0
for h in home:
    i = bisect.bisect(shop,h)#二部探索。shop[i] > h となる最小のiを返す。
    ans += min(abs(shop[i-1]-h),abs(shop[i]-h))
print(ans)