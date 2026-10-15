n = int(input())
a = list(map(int, input().split()))


for i in range(1, n):
    x = a[i]
    j = i - 1
    while (j >= 0) and (a[j] > x):
        a[j + 1] = a[j]
        j -= 1
        # j = -1で抜ける
    a[j + 1] = x

print(" ".join(map(str, a)))
