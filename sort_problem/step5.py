n, q = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = sorted(arr1)
for i in arr2:
    print(arr1[-i])
