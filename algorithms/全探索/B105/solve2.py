N = int(input())

total = 0
for n in range(1,N+1):
    divisor_cnt = 0
    for i in range(1,N+1):
        if n % i == 0:
            divisor_cnt += 1
    if divisor_cnt == 8 and n % 2 == 1:
        total += 1

print(total)
