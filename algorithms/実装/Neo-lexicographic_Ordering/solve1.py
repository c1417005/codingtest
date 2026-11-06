X = input()
N = int(input())
S = [input() for _ in range(N)]

S.sort(key = lambda s : [X.index(c) for c in s])
#key = にはsortが１つずつSから取り出して、lambdaに渡している
#lambda はその名前それぞれにindexを取り出すforループを回している。

print("\n".join(S))