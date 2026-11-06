import bisect

N = int(input())
A = sorted(map(int, input().split())) 
B = list(map(int, input().split()))
C = sorted(map(int, input().split()))

cnt = 0
for b in B:
    rst_a = bisect.bisect_left(A,b) #key 未満の数の個数
    rst_b = bisect.bisect_right(C,b) # key以下の数の個数
    cnt += rst_a * (N - rst_b) # keyより大きい数の個数

print(cnt)
