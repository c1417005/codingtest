#入力が max10^9だから２次元リストを持つと間に合わない。（10^18）
#そもそも解くのに必要ない
from bisect import bisect_left, bisect_right

H, W, N, Q = map(int, input().split())

rows, cols = [], []
for _ in range(N):
    r, c = map(int, input().split())
    rows.append(r)
    cols.append(c)
rows.sort()
cols.sort()
    

# queries = []
# for _ in range(Q):
#     queries.append(tuple(map(int, input().split())))


# for q in queries:
#     o,left,right = q
#     if o == 1:
#         print(Cs[(left-1):right].count(1))
#     elif o == 2:
#         print(Rs[(left-1):right].count(1))

# grid = [[0] * H for _ in range(W)]
# for k, v in dots:
#     grid[k - 1][v - 1] = 1

# grid_s =  [[0] * (H+1) for _ in range(W+1)]
# for k, v in dots:
#     grid_s[k - 1][v - 1] = 1

# for i in range(1,H):
#     for j in range(1,W):
#         grid_s[i+1][j+1] = grid_s[i][j] + grid[i][j]

out = []
for _ in range(Q):
    o,a,b = map(int,input().split())
    arr = rows if o == 1 else cols
    out.append(bisect_right(arr,b) - bisect_left(arr,b))

print("\n".join(map(str,out)))
# map :"3","3","1","8"
#join : "3\n3\n0\n5\n2\n1"
