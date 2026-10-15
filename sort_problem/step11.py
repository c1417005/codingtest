N, Q = map(int, input().split())
arr = list(map(int, input().split()))

queries = []
for i in range(Q):
    queries.append(tuple(input().split()))

for q, k, x in queries:
    k = int(k)
    if q == "get":
        a = sorted(arr, reverse=True)
        print(a[(k - 1)])

    elif q == "update":
        arr[k - 1] = int(x)
