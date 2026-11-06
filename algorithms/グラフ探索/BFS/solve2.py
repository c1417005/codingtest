from collections import deque


def main():

    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)

    dist = [-1] * N
    que = deque()

    dist[0] = 0
    que.append(0)

    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue

            dist[nv] = dist[v] + 1
            que.append(nv)

    for v in range(N):
        print(f"{v}:{dist[v]}")


main()
