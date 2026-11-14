n, m = map(int, input().split())

cnt = [0] * (n + 1)                 # cnt[c]: 誰も辞退しないときの c の得票数
g = [[] for _ in range(n + 1)]      # g[a]: 第一希望が a の投票者たちの第二希望
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    g[a].append(b)

    order = sorted((range(1,n+1)),key = lambda c:(-cnt[c],c))
    # -cnt[c] の値が小さい順で並び替え。（つまり得票が大きい順。）同じならcの値で比べる。
    top1,top2 = order[0],order[1]

    out = []
    for k in range(1,n+1):
        for b in g[k]:
            cnt[b] += 1

    if top1 != k:
        best = top1
    else:
        best = top2

    bc = cnt[best] #bestcount

    for b in g[k]:
        if cnt[b] > bc or (cnt[b] == bc and b < best):
            best = b
            bc = cnt[b]

    for b in g[k]:
        cnt[b] -= 1

    out.append(best)
for x in out:
    print(x)
