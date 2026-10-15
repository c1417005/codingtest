H = 5
W = 5

xyranges = [
    [(1, 1), (3, 3)],
    [(2, 2), (4, 4)],
    [(3, 3), (5, 5)],
    [(1, 3), (3, 5)],
    [(3, 1), (5, 3)],
]

arr = [[0] * (W + 2) for _ in range(H + 2)]

for (x1, y1), (x2, y2) in xyranges:
    arr[x1][y1] += 1
    arr[x1][y2 + 1] -= 1
    arr[x2 + 1][y1] -= 1
    arr[x2 + 1][y2 + 1] += 1

for h in range(1, H + 1):
    for w in range(1, W + 1):
        arr[h][w] += arr[h][w - 1] + arr[h - 1][w] - arr[h - 1][w - 1]

print(max(map(max, arr)))
