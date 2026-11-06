#inf はメモリを食わない。or 10**18
N,M,X = map(int,input().split())

ref_prices = []
points = []
for _ in range(N):
    c,*a = map(int,input().split())
    ref_prices.append(c)
    points.append(a)

min_money = float('inf')
for i in range(1 << N):
    ok = False
    scores = [0]*M
    money = 0
    for j in range(N):
        
        if ((i >> j) & 1):
            money += ref_prices[j]
            # print(i,j,money)
            for k in range(len(points[j])):
                scores[k] += points[j][k]

            for score in scores:
                if score >= X:
                    ok = True
                else:
                    ok = False
                    break
    if ok:
        min_money = min(min_money,money)

if money != 0 and ok != True:
    min_money = -1


print(min_money)







