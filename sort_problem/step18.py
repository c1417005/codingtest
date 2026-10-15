n = int(input())
hash_table = [[] for x in range(10)]

for i in range(n):
    num = int(input())
    h = num % 10
    hash_table[h].append(num)

for i in range(10):
    print(*hash_table[i])
