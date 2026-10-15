n = int(input())
x = [int(input()) for _ in range(n)]
x.sort()
T = 777

answers = []
for i in range(1 << n):
    # 1をn桁左にずらす。(2進)→10進
    # n=3 1000(2) →8(10) 2^3回
    ans = []
    total = 0
    for j in range(n):
        if (i >> j) & 1:
            # n=3 0,1,2の3回
            # iを右にj桁ずらして（右桁のj桁を捨てる）一番右の1桁だけ取り出す。
            # iのj桁目は1か？
            ans.append(x[i])
            total += x[i]
            if total == 777:
                answers.append(ans)
    l = len(answers)
    if l == 0:
        print("no answers")
    elif l == 1:
        print(*answers[0])
    else:
        print("multiple answers")
