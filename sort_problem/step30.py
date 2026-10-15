N = int(input())
arr = list(map(int,input().split()))

K = 0
sum1 = [0]*(N+1)
for i in range(1,N+1):
    sum1[i] = sum1[i-1] + arr[i-1]
sum2 = [0]*(N+1)
for i in range(1,N+1):
      sum2[i] = sum1[N] - sum1[i]

best = float('inf')
for j in range(1,N+1):
        best = min(best,abs(sum1[j]-sum2[j]))

print(best)


# 1 2 3
# 0 1 3 6
# 0 5 3 0
# 6-1 6-3 6-
