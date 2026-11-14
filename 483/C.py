N,M = map(int,input().split())
votes = [tuple(map(int,input().split())) for _ in range(M)]

#O(NM)にならない方法を考えたい
for i in range(1,N+1):
    result = dict.fromkeys(range(1,N+1),0)
    for k,v in votes:
        if k == i:
            result[v] += 1
        else:
            result[k] += 1
    max_key = max(result, key=lambda c: result[c])
    print(max_key)