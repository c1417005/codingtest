from bisect import bisect_left, bisect_right

H,W,N = map(int,input().split())
dots = []
a = b = []
for _ in range(N):
    dot = tuple(map(int,input().split()))
    dots.append(dot)
    a.append(dot[0])
    b.append(dot[1])


n_a = bisect_right(a,)




    



