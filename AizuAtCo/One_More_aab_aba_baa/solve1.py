import itertools

ip = input().split()
S = sorted(ip[0])
K = int(ip[1])

s = list(set(itertools.permutations(S)))
print("".join(s[K-1]))
# print(s)
