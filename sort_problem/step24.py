arr = [1,5,9,7,5,3,2,5,8,4]

even = [0]*10

for i in range(len(even)):
    if arr[i] % 2 == 0:
        even[i] = 1

s = [0]*10

for i in range(1,len(even)):
    s[i] = s[i-1] + even[i]
print(s[7]-s[2])
