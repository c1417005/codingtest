N,K = map(int,input().split())
A = list(map(int,input().split()))


def coins(x):
    c = 0
    while x > 0:
        d = x % 10 #一番右の桁を取り出す
        c += d // 5 + d % 5 # ５以上なら1 + 5で払った残り
        x //= 10 #一番右を捨てる
        return c


def func(start,cnt,total):
    if cnt == K:
        return coins(total)

    best = float('inf')
    # for i in range(N):
    #     total += A[i]
    #     best = min(price,func(num+i,total,A))
    for i in range(start,N):
        best = min(best,func(i + 1,cnt + 1,total+A[i]))
    return best