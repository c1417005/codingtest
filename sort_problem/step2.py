n, k = map(int,input().split())
arr = list(map(int, input().split()))

def find_kth(n,k,arr):
    if n == 1:
        print(arr[0])
        return

    for i in range(n-1):
        for j in range(n-1,i,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    # arr.sort()

    print(arr[-k])

find_kth(n,k,arr)