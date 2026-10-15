while True:
    n,x = map(int,input().split())
    if n == 0 and x == 0:
        break

    comb_cnt = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                if i + j + k == x:
                    comb_cnt += 1
    
    print(comb_cnt)