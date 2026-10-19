N,K = map(int,input().split())
A = list(map(int,input().split()))

# coins = [10 ** i for i in range(10)]

def coins(x):
    c = 0
    while x > 0:
        d = x % 10 #桁数
        c += d // 5 + d % 5 #コインの枚数
        x //= 10
    return c

def func (start,cnt,total):
    if cnt == K:
        return coins(total)

    best = float('inf')
    for i in range(start,N):
        best = min(best,func(i + 1,cnt + 1,total + A[i]))
    return best

print(func(0,0,0))