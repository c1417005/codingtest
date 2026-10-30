n, W = map(int, input().split())
value = []
weight = []
for _ in range(n):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)

# 初期条件 : dp[0][w] = 0
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(n):
    for w in range(W + 1):#0~W 
        if w >= weight[i]:
            dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
        else:
            dp[i + 1][w] = dp[i][w]

print(dp)