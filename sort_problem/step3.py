n = int(input())
arr = list(map(int, input().split()))

arr.sort()


def del_repeat(n, arr):
    unique_arr = []
    for i in range(n):
        if i == 0 or arr[i] != arr[i - 1]:
            unique_arr.append(arr[i])

    # or
    # unique = set(a)

    print(*unique_arr)  # リストの中身を空白区切りで


del_repeat(n, arr)
