n = int(input())
arr = list(map(int, input().split()))


def find_max_min(n, arr):
    if n == 1:
        print(arr[0])

    min_index = 0
    max_index = 0

    for i in range(n):
        if arr[min_index] > arr[i]:
            min_index = i
        if arr[max_index] < arr[i]:
            max_index = i
    print(arr[max_index], arr[min_index])


find_max_min(n, arr)
