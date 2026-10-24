n = int(input())
S = list(input().split())
q = int(input())
T = list(input().split())

cnt = 0

def is_Ok(mid,key):
    return S[mid] >= key

def binary_search(key):
    left = -1
    right = len(S)

    while right - left > 1:
        mid = (left + right) // 2
        if is_Ok(mid,key):
            right = mid

        else:
            left = mid

    return right

for t in T:
    if binary_search(t) != n:
        cnt += 1
print(cnt)


