N,M,Q = map(int,input().split())
arr = []
for n in range(N):
    arr.append(list(map(int,input().split())))

prefix_arr = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        prefix_arr[i+1][j+1] = arr[i][j]
print(prefix_arr)

for i in range(N):
    for j in range(M):
        prefix_arr[i+1][j+1] += (prefix_arr[i][j+1] + prefix_arr[i+1][j] - prefix_arr[i][j]) 
print(prefix_arr)

def compute_prefix(Q):
    a,b,c,d = map(int,(input().split()))
    print(prefix_arr[c+1][d+1] - prefix_arr[a][d+1]- prefix_arr[c+1][b] + prefix_arr[a][b])

for _ in range(Q):
    compute_prefix(Q)

