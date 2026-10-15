def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr

    p = arr[0]

    arr1,arr2 = div(p,arr[1:])

    return quick_sort(arr1) + [p] + quick_sort(arr2)



def div(p,arr):

    left,right = [],[]
    for i in arr:
        if i < p:
            left.append(i)
        else:
            right.append(i)

    return left,right
