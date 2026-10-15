MAX = 5
stack = [0]*MAX
sp = 0

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp +1
        print("データ",d,"を追加しました")
    else:
        print("これ以上データを入れられませんでした")

def pop():
    global sp
    if sp > 0:
        sp = sp-1
        #push後、sp = 5,index0~4
        return stack[sp]
    else:
        print("取り出すデータが存在しませんでした")
        return None

for i in range(6):
    push(i)
for i in range(6):
    d = pop()
    print("取り出したデータ",d)