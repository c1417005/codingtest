s = input()
# 一文字ずつ取り出したい(s[0] = "9"など)ので文字列で受け取る
d = len(s)
# 桁数

ans = 0
for bit in range(1 << d):
    a,b = [],[]
    for i in range(d):
        if (bit >> i) & 1:
            a.append(s[i])
        else:
            b.append(s[i])

    if not a or not b:
        continue

    a.sort(reverse=True)
    b.sort(reverse=True)

    if a[0] == '0' or b[0] == '0':
        continue

    ans = max(ans,int(''.join(a)) * int(''.join(b))) 

print(ans)


