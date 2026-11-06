n,A = map(int,input().split())
a = list(map(int,input().split()))

#dp[i][j]:先頭i個の整数からいくつかえらんで合計jにできるか
dp = [[False] * (A+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(A+1):
        dp[i+1][j] |= dp[i][j]

        if j >= a[i]:# 「合計 j が a[i] 以上のときだけ、a[i] を選ぶ場合を考える
            dp[i+1][j] |= dp[i][j-a[i]] #(j - 今選んだ数字) がTrue だったら、足してj になるのでTrue

        # if j >= a[i]:
        #     dp[i + 1][j] = dp[i][j] or dp[i][j - a[i]]
        # else:
        #     dp[i + 1][j] = dp[i][j]
        
print("YES" if dp[n][A] else "NO")