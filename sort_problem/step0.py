n = int(input())
arr = list(map(int, input().split()))


def is_upper(n, arr):
    if n <= 1:
        print("Yes")
        return

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                print("No")
                return
    print("Yes")


is_upper(n, arr)
