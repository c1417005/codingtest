n, l, r = map(int, input().split())
arr = list(map(int, input().split()))

print(*(arr[: l - 1] + sorted(arr[l - 1 : r - 1]) + arr[r - 1 :]))
