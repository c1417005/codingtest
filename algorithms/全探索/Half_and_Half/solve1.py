A, B, C, X, Y = map(int, input().split())

min_cost = A*X + B*Y
for ab_pairs in range(max(X, Y) + 1):
    buy_a = max(0, X - ab_pairs)
    buy_b = max(0, Y - ab_pairs)
    cost = A * buy_a + B * buy_b + C * (2 * ab_pairs)
    min_cost = min(min_cost, cost)
print(min_cost)