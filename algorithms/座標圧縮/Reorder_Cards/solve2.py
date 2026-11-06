from bisect import bisect_left,bisect_right

H,W,N = map(int,input().split())
dots = []
R,C = [],[]
for _ in range(N):
    dot = tuple(map(int,input().split()))
    dots.append(dot)
    R.append(dot[0])
    C.append(dot[1])

ur = sorted(set(R))
uc = sorted(set(C))

out = []
for r,c in zip(R,C):
    #「残る行を上から並べたとき、自分が何番目か」
    out.append(f"{bisect_right(ur,r)} {bisect_right(uc,c)}")
print("\n".join(out))