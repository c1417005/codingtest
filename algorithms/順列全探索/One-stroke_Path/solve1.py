import itertools
N,M = map(int,input().split())

arr = []
for _ in range(M):
    #グラフはM辺だから。
    arr.append(tuple(map(int,input().split())))

adjacency_matrix = [[0]*N for _ in range(N)]
for a in arr:
    adjacency_matrix[a[0]-1][a[1]-1] += 1
    adjacency_matrix[a[1]-1][a[0]-1] += 1


count = 0
for p in itertools.permutations(range(1,N)):
    path = [0] + list(p)
    #0(頂点1)始まりの順列（N頂点のたどりうる全場合）を作る
    if all(adjacency_matrix[path[i]][path[i+1]] for i in range(N-1)):
        count += 1
        #1→Nまですべての頂点を通っていくということは、N-1回移動する。
        #path[i]行目のpath[i+1]番目が１か調べる。

print(count)
