n = int(input())
arr = list(map(int, input().split()))

ball_stack = []

for a in arr:
    
    while ball_stack and ball_stack[len(ball_stack) - 1] == a:
        ball_stack.pop()
        a *= 2
       
    ball_stack.append(a)




for i in range(len(ball_stack) - 1, -1, -1):
    print(ball_stack[i])
