n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr.sort(key = lambda x:(len(x),*x))

for a in arr:
    print(a)