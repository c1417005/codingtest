result = []
numbers = [x for x in range(2,101)]

def prime_checker(n):
    for i in range(2,int((n)/2)+1):
        if n % i == 0:
            return
    result.append(n)
        # 追加はループの外で1回行いたい
    
def main():
    for j in numbers:
        prime_checker(j)

main()
print("primes:",result)
