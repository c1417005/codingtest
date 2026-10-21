from collections import deque

def main():
    N,M = map(int,input().split())

    G = [[] for _ in range(N)] # グラフ
    for _ in range(M):
        a,b = map(int,input().split())
        G[a].append(b) # 頂点aからの辺を登録
        # G[b].append(a)  # 無向グラフなら往復分登録

    dist = [-1]*N # （頂点0からの）距離distance
    que = deque() # 探索候補の頂点

    # 初期化
    dist[0] = 0
    que.append(0)

    while que:
        v = que.popleft() #頭から１つ頂点取り出す vertex
        for nv in G[v]:

            #探索済みならスキップ
            if dist[nv] != -1:
                continue

            dist[nv] = dist[v] + 1 #今調べてる頂点+1
            que.append(nv)

    for v in range(N):
        print(f"{v}: {dist[v]}")

main()