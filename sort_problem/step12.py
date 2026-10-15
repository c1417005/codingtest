from collections import deque

N, X = map(int, input().split())
arr = list(map(int, input().split()))

q = deque(arr[:X])

left = q[0]
current = sum(q)
max_result = current
left = q[0]

for a in arr[X:]:
    out = q.popleft()
    q.append(a)
    # max_result = max_result - q[0] + a    q[0]の更新タイミングでバグる
    current = current - out + a
    if current > max_result:
        max_result = current
        left = q[0]


print(max_result, left)
