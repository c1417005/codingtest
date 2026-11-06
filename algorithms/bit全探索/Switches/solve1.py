N,M = map(int,input().split())
# N:スイッチの数。M:電球の数。
switches = []
for _ in range(M):
    k,*s = map(int,input().split())
    #入力を頭とそれ以外で別の変数に代入
    switches.append(s)
p = list(map(int,input().split()))

ans = 0
for bit in range(1 << N):
    #1を左にN個ずらす。(1 << 2) = 100(2) = 4(10) range(4)なので0~3。 選ぶ・選ばないの2^N
    #スイッチの点灯パターンを一つ選ぶ
    ok = True
    for i in range(M):
        #そのパターンで電波を１つずつ調べる
        cnt = 0
        for s in switches:
            #その電球に繋がったスイッチを１つずつ見る
            if (bit >> (s-1)) & 1:
                #bitを(s-1)桁右にずらす。s桁目（右から）を一番右に持ってくる。
                #&1で一番右の桁を取り出し1ならスイッチsはon
                cnt += 1
        if cnt % 2 != p[i]:
            #on の数がp[i]と一致しなければそこでループを１つ抜ける。
            ok = False
            break
    if ok:
        ans += 1
print(ans)