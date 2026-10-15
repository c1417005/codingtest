def recursive_sum(n):
    if n <= 0:
        return n
    return n + recursive_sum(n - 1)


# コールスタック returnくるまで積みあがっていく。
