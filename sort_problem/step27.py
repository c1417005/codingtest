a = [1, 5, 9, 1, 20, 5, 3, 6, 5, 4]
K = 15

left = 0
s = 0
count = 0
best = 0  # 最長区間の長さ

for right in range(len(a)):
    s += a[right]
    while s > K:
        s -= a[left]
        left += 1
    count += right - left + 1

print(count)
