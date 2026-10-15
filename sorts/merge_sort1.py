import math

INF = math.inf
count = 0


def merge(A, left, mid, right):
    global count
    nl = mid - left
    nr = right - mid

    L = [A[left + i] for i in range(nl)]
    R = [A[mid + i] for i in range(nr)]

    L.append(INF)
    R.append(INF)

    lindex = 0
    rindex = 0

    for i in range(left, right):
        if L[lindex] < R[rindex]:
            A[i] = L[lindex]
            lindex += 1
        else:
            A[i] = R[rindex]
            rindex += 1
            count += 1


def merge_sort(A: list[int], left: int, right: int):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)
