N = int(input())
A = list(map(int,input().split()))
X = int(input())

k = 0
total = 0

total_a = sum(A)
q = X // total_a
r = X % total_a

while total <= r:
    i = k % N
    total += A[i]
    k += 1

print(q*len(A) + k)