Q = int(input())
# arr = []
# for _ in range(Q):
#     k = tuple(map(int,input().split()))
#     arr.append(k)


# for left,right in arr:
#     l,r = []
#     while(left >= 0):
#         l.append(1)
#         left = left - 15


#     while(right >= 0):
#         r.append(1)
#         right = right - 15

#     suml,sumr = [0]
#     for i in range(1,len(l)):
#         suml.append(suml[i-1] + 1))

queries = []
for _ in range(Q):
    L, R = map(int, input().split())
    queries.append((L, R))

N = 0
for L,R in queries:
    if R > N:
        N = R

cnt = [0]*(N+1)
for i in range(1,N+1):
    if i % 15 == 0:
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]

for L,R in queries:
    print(cnt[R] - cnt[L-1])
    
        