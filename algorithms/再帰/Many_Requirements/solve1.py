N,M,Q = map(int,input().split())
queries = [list(map(int,input().split())) for _ in range(Q)]

# 戻り値の型 func(引数) {
#   if (ベースケース) {
#     return ベースケースに対する値;
#   }
  
#   func(次の引数); // 再帰呼び出しします。その前後でも色々やります。
#   return (答え);
# }

def score(A):
    s = 0
    for a,b,c,d in queries:
        if A[b-1] - A[a-1] == c:
            s += d
    return s


def func(cur):
    #ベースケース N要素の数列ができたらscoreを計算し、返す。
    if (len(cur) == N):
        return score(cur)
    
    
    start = cur[-1] if cur else 1 #直前 or 1(まだcurが空の時)
    best = 0
    for v in range(start,M+1):
        cur.append(v)
        best = max(best,func(cur))
        cur.pop() #N-1桁まで決まったあと、N通り試すため
    return best

print(func([]))

    