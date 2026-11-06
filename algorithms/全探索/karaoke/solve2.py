N,M = map(int,(input().split()))
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

total_best = 0
for left in range(M):
    for right in range(left + 1,M):
        total = 0
        for a in arr:
            stu_best = max(a[left],a[right])
            total += stu_best
        total_best = max(total_best,total)
print(total_best)