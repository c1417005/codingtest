N = int(input())

cnt = 0
for n in range(1,N+1):
    #Nまでループ
    cnt_divisor = 0
    for i in range(1,n+1):
        if n % i == 0:
            cnt_divisor += 1
            #それぞれについてnまでループ
            #約数の数を数える

    if cnt_divisor == 8 and n % 2 == 1:
        cnt += 1
        #抜けたら参照。カウント+1
        

print(cnt)
