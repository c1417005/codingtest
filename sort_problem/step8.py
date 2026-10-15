n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: x[1])

count = 0
e = 0
for start, end in arr:
    if e < start:
        count += 1
        e = end

print(count)

# スケジューリング
# たしかにソートの問題だった。
# s:eで数字をrangeでつくって確かめていくという方法は非効率だし、実装も複雑。
