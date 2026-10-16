# 「正直者」か「真偽不明な人」。
# 真偽不明な人は、正しくても間違っててもいい。ので無視。
#正直者は絶対正しくないといけない。→ 仮説との矛盾をチェックする

N = int(input())

testimony_by_people = []
for _ in range(N):
    a = int(input())
    testimony = []
    for _ in range(a):
        testimony.append(tuple(map(int,input().split())))
    testimony_by_people.append(testimony)

best = 0
for i in range(1<<N):#bit は ...321 の順 
    ok = True
    for j in range(N):
        #仮定に対して証言者のループ
        if not ((i>>j) & 1):
            #不適切なら無視して次の判定へ
            continue
        for x,y in testimony_by_people[j]:
            if ((i >> (x-1)) & 1) != y:
                #食い違ったら
                ok = False
                break
        if not ok:
            #j+1に進まないように
            break
    if ok:
        best = max(best,bin(i).count('1'))

print(best)