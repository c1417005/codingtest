N = int(input())
S = input()

cnt = 0
for i in range(1000):
    pas = f"{i:03}"
    #000~999
    idx = -1
    ok = True
    for c in pas:
        #pasから１文字ずつ取り出す
        idx = S.find(c,idx + 1)
        #c が(idx + 1)番目から右以降にあるか探す。
        #普通のinだと連続しか発見できない
        if idx == -1:
            #-1が返ったら「見つからなかった」
            ok = False
            break
    if ok:
        cnt += 1


print(cnt)
