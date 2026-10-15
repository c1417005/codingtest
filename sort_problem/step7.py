n, m, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(
    key=lambda x: (x[k - 1], *x)
)  # arrの各要素xについて、x[k-1]を戻している。補助キー（*x）と指定しないと、kが同じ場合は入力順になる。

for a in arr:
    print(*a)
