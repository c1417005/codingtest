N = int(input())

inp = ["B"]
arr = []
def solve(N):
    if N == 1:
        return

    if N % 2 != 0: # if の中で solve(N) を呼んだあと、戻ってきて N //= 2 以降も実行されます。そのため、同じ数を二重に処理します。return を入れるか else にする必要があります。
        N = N-1
        arr.append("B")
        print(N)
        solve(N)

    N //= 2
    arr.append("A")
    print(N)
    solve(N)
    

# print(solve(N))
solve(N-1)
print(arr)

