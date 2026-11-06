n,m = map(int,input().split())

arr = []
for _ in range(m):
    arr.append(tuple(map(int,input().split())))

adjacency_matrix = [[0]*n for _ in range(n)]

for a in arr:
    adjacency_matrix[a[0]-1][a[1]-1] += 1
    adjacency_matrix[a[1]-1][a[0]-1] += 1


for row in adjacency_matrix:
    print(*row)