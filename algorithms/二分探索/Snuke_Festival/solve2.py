N = int(input())
A = sorted(map(int, input().split())) # 二部探索はソート済み配列にしか使えない
B = list(map(int, input().split()))
C = sorted(map(int, input().split()))

#lowerは範囲の左端。upperは範囲の右端の１つ後ろを返す。

#bisect_left
#key 未満の数の個数
def lower_bound(arr,key):
    left,right = -1,N
    while right - left > 1:
        mid = (left+right) // 2
        if arr[mid] >= key:
            right = mid
        else:
            left = mid
    return right

#bisect_right
#key 以下の個数
def upper_bound(arr,key):
    left,right = -1,N
    while right - left > 1:
        mid = (left+right) // 2
        if arr[mid] > key:
            right = mid
        else:
            left = mid
    return right

cnt = 0

for b in B:
    num_a = lower_bound(A,b)
    num_c = N - upper_bound(C,b)
    cnt += num_a * num_c
print(cnt)