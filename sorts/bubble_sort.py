n = int(input())
a = list(map(int,input().split()))

for i in range(n-1):
    for j in range(n-1,i,-1):#２番目の引数で指定した"直前"までいく。
        if a[j-1] > a[j]:
            a[j-1],a[j] = a[j],a[j-1]
        print(" ".join(map(str,a)))