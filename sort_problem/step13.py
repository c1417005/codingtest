n = int(input())
arr = list(input().split())

stack = []
for a in arr:
    if a not in ("+", "-"):
        stack.append(a)
    else:
        x = int(stack.pop())
        y = int(stack.pop())
        stack.append(eval(f"{y} {a} {x}")) #eval:文字列を式として計算

print(stack.pop())
