N = int(input())
arr = []


def solve(n):
    if n == 0:
        return
    if n % 2 == 1:
        arr.append("A")
        solve(n - 1)

    else:
        arr.append("B")
        solve(n // 2)

solve(N)
print("".join(reversed(arr)))
