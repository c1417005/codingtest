S = list(input())

ACGT = "ACGT"

max_length = 0
for start in range(len(S)):
    for end in range(start,len(S)):
        if S[end] not in ACGT:
            break
        #breakしなかった上で計算。breakしてからだと余分に数える
        max_length = max(max_length,end - start + 1)
    # print(S[start])
    # print(S[end])
    # print(max_length)
print(max_length)