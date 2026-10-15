N, Q = map(int, input().split())

arr = [0] * (N + 2)
for q in range(Q):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b + 1] -= 1

s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + arr[i]

print(max(*s))
