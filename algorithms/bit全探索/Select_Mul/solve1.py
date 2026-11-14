s = input()
# 一文字ずつ取り出したい(s[0] = "9"など)ので文字列で受け取る
d = len(s)
# 桁数

ans = 0
for bit in range(1 << d):
# 1をdビット左にずらす。値は2^d。
# 0 <= bit <= 2^d-1
    a,b = [],[]
    for i in range(d):
        if (bit >> i) & 1:
        # bitは000 ~ 111...
        # #そのi桁目が１かどうか調べる。
        #i 桁目が1 なら s[i] をaに入れる。
            a.append(s[i])
        else:
            b.append(s[i])

    if not a or not b: #a と b は空になってはいけない
        continue

    a.sort(reverse=True)
    b.sort(reverse=True)

    if a[0] == '0' or b[0] == '0':#leading_zero をはじく
        continue

    ans = max(ans,int(''.join(a)) * int(''.join(b))) #int()関数に配列の中身を合体させて渡す。

print(ans)


