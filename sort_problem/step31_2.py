Q = int(input())

# クエリを読み込む
queries = []
for _ in range(Q):
    L, R = map(int, input().split())
    queries.append((L, R))

# 表をどこまで作るか（一番大きい R まで）
N = 0
for L, R in queries:
    if R > N:
        N = R

# 累積和の表を作る
# 0 ... 15 ... 29,30,31...
# 0 ...  1  ... 1 ,3,3 ...

# cnt[i] = 1〜i に含まれる15の倍数の個数
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    if i % 15 == 0:
        cnt[i] = cnt[i - 1] + 1  # 15の倍数なら1増やす
    else:
        cnt[i] = cnt[i - 1]  # そうでなければ前と同じ

# 各クエリに答える
for L, R in queries:
    print(cnt[R] - cnt[L - 1])
    # L から Rまで → Lは残さないといけない。
