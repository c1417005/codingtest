a = [1, 5, 9, 1, 20, 5, 3, 6, 5, 4]
K = 15

s = 0
left = 0
count = 0
best = 0

for right in range(len(a)):
    s += a[right]
    while s > K:
        s -= a[left]
        left += 1
    count += right - left + 1
    best = max(best, right - left + 1)

print(best)
