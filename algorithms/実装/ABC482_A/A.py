S = input()# 文字列はイテレータ。入力によってはシンプルにinputでいい。
# print(S)
cnt = 0
for s in S:
    if s == "o":
        cnt += 1

print("even" if cnt % 2 == 0 else "odd")