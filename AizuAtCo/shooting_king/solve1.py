#  二部探索
# 「直接答えを求める(得点を計算して最小を求める)」から「あてずっぽうな条件の判定（得点をX以下にできる？）」
#  へ発送を転換する。

N = int(input())
h, s = [], []
for _ in range(N):
    hi, si = map(int, input().split())
    h.append(hi)
    s.append(si)

INF = 1 << 60
left, right = 0, INF
while right - left > 1:
    mid = (left + right) // 2

    ok = True
    t = []
    for i in range(N):
        if mid < h[i]:
            ok = False
            break
        t.append((mid - h[i]) // s[i]) # 道のり/速さ ＝ 時間

    if ok:
        t.sort()
        for i in range(N):# i は秒数
            if t[i] < i: #タイムリミットが近い順に並べて、間に合わなかったら
                ok = False
                break

    if ok:# 風船すべて制限時間に間に合った。
        right = mid
    else:
        left = mid

print(right)