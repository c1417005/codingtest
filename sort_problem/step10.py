n = int(input())
arr = []

for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: (abs(x[0]) + abs(x[1]), *x))

for a in arr:
    print(*a)
