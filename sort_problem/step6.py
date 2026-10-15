n = int(input())
arr = []
for i in range(n):
    l, r = map(int, input().split())
    arr.append((l, r))

arr.sort()
for a in arr:
    print(*a)
