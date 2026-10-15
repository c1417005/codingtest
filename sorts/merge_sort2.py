def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0  # left
        j = 0  # right
        k = 0  # merged
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1

            else:
                arr[k] = right_arr[j]
                j += 1

            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1 


test_arr = [3, 5, 4, 2, 5, 2, 0, 2, 5]
merge_sort(test_arr)
print(test_arr)
