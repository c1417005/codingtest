# A,Bをソートして単調増加性を利用して最小値を探していく。

def main():
    n,m = map(int,input().split())
    a = sorted(map(int,input().split()))
    b = sorted(map(int,input().split()))

    i =  j = 0
    ans = float('inf')
    while i < n and j < m:
        d = a[i]-b[j]
        if d == 0:
            print(0)
            return
        if d < 0:
            ans = min(ans,-d)
            i += 1
        else:
            ans = min(ans,d)
            j += 1
    print(ans)

main()

