ranges = [(1,3),(1,8),(3,8),(3,6),(7,9)]

arr = [0]*12

for r in ranges:
    a,b  = r
    arr[a] += 1
    arr[b+1] -= 1

s = [0]*11

for i in range(1,len(s)):
    s[i] = s[i-1] + arr[i]

print(*s[1:])
