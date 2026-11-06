N,M,Q = map(int,input().split())
queries = [list(map(int,input().split())) for _ in range(Q)]

# adj = [[0]*N for _ in range(N)]


def score(A):
    s = 0
    for q in queries:
        a,b,c,d = q
        if A[b-1] - A[a-1] == c:
            s += d
    return s

def func(start,A):

    if len(A) == N:
        return score(A)
    
    start = A[-1] if A else 0
    best = float('-inf')
    for i in range(start,M):
        A.append(i)
        best = max(best,func(i+1,A))
        A.pop()
    
    return best

print(func(0,[]))