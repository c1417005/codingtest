N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))


total_best = 0
for left in range(M):
    for right in range(left + 1, M):   # left < right で重複なしの全ペア
        total = 0                        # ペアごとにリセット
        for a in arr:
            #left,right を固定したうえで、列を回していく。
            total += max(a[left], a[right])
        total_best = max(total_best, total)  # 生徒全員を回した後に比較

print(total_best)

# for _ in range(len(arr)):
#     total = 0
#     stu_best = 0
#     total_best = 0
#     for a in arr: 
#         for i in range(M):
#             for j in range(1,M):
#                 stu_best = max(a[i],a[j])
#             total += stu_best
#         total_best = max(total,total_best)

# left,right = 0,1
# total = 0

# for a in arr:
#     stu_best = max(a[left],a[right])
#     total += stu_best

#     total_best = max(total_best,total)
#     left 



# print(total_best)

