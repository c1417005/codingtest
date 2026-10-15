arr = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
sums = [0]

for i in range(1, len(arr)):
    sums.append(sums[i - 1] + arr[i])


print(sums[7] - sums[2])
