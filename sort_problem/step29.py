N, A, B = map(int, input().split())
words = list(input())

arr = [0] * (N + 1)
i = 0

while i <= N - 3:
    if words[i] == "p" and words[i + 1] == "i" and words[i + 2] == "z":
        arr[i + 2] = 1
        i += 2
    else:
        i += 1

# 今1-indexで考えている。
# このとき、p >= A ⇒ z >= A +2   A +2 <= z <= B
# 0-indexで考えると、
# A+1 <= z <= B-1



s = [0] * (N + 1)
for n in range(1, N + 1):
    s[n] = s[n - 1] + arr[n]

print(s[B-1] - s[(A+1-1)]) # 累積和はそもそも左端は-1する。

# [l,r) l以上r未満