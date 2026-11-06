N,M = map(int,input().split())
# N:スイッチの数。M:電球の数。
switches = []
for _ in range(M):
    k,*s = map(int,input().split())
    # 入力を頭とそれ以外で別の変数に代入
    switches.append(s)
p = list(map(int,input().split()))

ans = 0
for bit in range(1<<N):
    ok = True
    for i in range(M):
        cnt = 0 
        for s in switches:
            if ((bit >> (s-1)) & 1):
                cnt += 1
        if p[i] != (cnt % 2):
            ok = False
            break
    if ok:
        ans += 1

print(ans)
            