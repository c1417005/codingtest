H, W = 5, 5
a = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9],
]

s = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(H):
    for j in range(W):
        s[i+1][j+1] = a[i][j]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]

print(s[4][4] - s[1][4] - s[4][1] + s[1][1])  # 45