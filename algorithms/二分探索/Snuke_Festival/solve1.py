N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

cnt = 0

def is_Ok(arr,mid,key):
    return arr[mid] >= key

def binary_search(arr,key):
    left = -1
    right = N

    while right - left > 1:
        mid = (left + right) // 2
        if is_Ok(arr,mid,key):
            right = mid
        else:
            left = mid

    return right

for a in A:
    if binary_search(B,a) != N:
        for b in B:
            if binary_search(C,b) != N:

                cnt += 1
print(cnt)

#結果は 2 ですが、正解は 3 です（(1,2,3), (1,2,6), (1,4,6)）。
# b=2 のとき c の候補が 3 と 6 の2個あるのに、1回しか数えていません。