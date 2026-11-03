from bisect import bisect_right

H,W,N = map(int,input().split())
R,C = [],[]
for _ in range(N):
    ri,ci = map(int,input().split())
    R.append(ri)
    C.append(ci)

ur = sorted(set(R))
uc = sorted(set(C))

out = []
for r,c in zip(R,C):
    out.append(f"{bisect_right(ur,r)} {bisect_right(uc,c)}") #集合の中で、座標は何番目か。

print("\n".join(out))