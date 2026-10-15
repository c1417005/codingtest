from collections import deque


N, K = map(int, input().split())
arr = list(map(int, input().split()))

ele_queue = deque()


# count = 0
for a in arr:
    while (
        ele_queue and ele_queue[0] + K >= a
    ):  # whileは毎回Nで回るわけではない。よってO(n)
        ele_queue.popleft()
    ele_queue.append(a)
    print(len(ele_queue))
