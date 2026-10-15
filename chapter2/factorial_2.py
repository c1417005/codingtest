def factrial(n):
    if n == 0:
        return 1
    else:
        return n * factrial(n-1)

# n * (n-1) * ・・・ * 1 になるので計算できる。

for i in range(0,21):
    print(f"{i}! = {factrial(i)}")