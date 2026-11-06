import itertools
#順列全探索

ip = input().split()
S = sorted(ip[0])
K = int(ip[1])

s = list(set(itertools.permutations(S)))
#同じ文字が含まれる場合重複もできるので、setで消す
print("".join(s[K-1]))
# print(s)
