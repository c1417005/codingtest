import itertools

N = int(input())

S = []
for i in range(2):
    S.append(tuple(map(int,input().split())))

seqs = list(itertools.permutations(range(1,N+1)))
# permutationsの各要素はタプル

a = seqs.index(S[0])
b = seqs.index(S[1])

print(abs(a-b))
