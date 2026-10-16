# inf はメモリを食わない。or 10**18
N, M, X = map(int, input().split())

ref_prices = []
points = []
for _ in range(N):
    c, *a = map(int, input().split())
    ref_prices.append(c)
    points.append(a)

INF = float("inf")
min_money = INF

for i in range(1 << N):
    ok = False
    scores = [0] * M
    money = 0
    for j in range(N):
        if (i >> j) & 1:
            money += ref_prices[j]
            
            for k in range(M):#len(points[j])は要はM
                scores[k] += points[j][k]

            
            if all(s >= X for s in scores):
                #中身が全部True なら True。１つでもFalseならFalse
                #一つでもTrue ならTrue返したければany
                min_money = min(min_money,money)
  
print(min_money if min_money != INF else -1)

print(min_money)
