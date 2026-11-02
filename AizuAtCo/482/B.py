S = []
N = 5 #Sのlen 

for _ in range(N):
    S.append(list(input()))# 文字列を１文字ずつ格納したいとき。１文字ずつ見ていきたいとき。
# print(S)

cnt_h = 0
cnt_v = 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if S[i][j] == "o":
            cnt += 1
        cnt_h = max(cnt_h,cnt)

for j in range(N):
    cnt = 0
    for i in range(N):
        if S[i][j] == "o":
            cnt += 1
        cnt_v = max(cnt_v,cnt)

k,l = 0,0
cnt_n = 0
while k < 5 and l < 5:
    if S[k][l] == "o":
        cnt_n += 1
    
    k += 1
    l += 1

q,r = 4,0
cnt_r_n = 0
while q > 0:
    if S[q][r] == "o":
        cnt_r_n += 1

    q -= 1
    r += 1


print(5 - max(cnt_h,cnt_v,cnt_n,cnt_r_n))
# print(cnt_h,cnt_v,cnt_n,cnt_r_n)


