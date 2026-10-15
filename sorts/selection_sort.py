n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    if min_index != i:
        a[i], a[min_index] = a[min_index], a[i]

print(" ".join(map(str, a)))
