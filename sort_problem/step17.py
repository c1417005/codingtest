n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

rs = []
hash_table = [-1] * 10
for num in nums:
    count = 1
    h = num % 10
    while h in rs:
        h = ((num) + count) % 10
        count += 1
    # while table[hash] != -1:
    #     hash = (hash + 1) % 10   -1じゃない＝すでにあった。
    rs.append(h)
    hash_table[h] = num

for j in range(len(hash_table)):
    print(hash_table[j])
