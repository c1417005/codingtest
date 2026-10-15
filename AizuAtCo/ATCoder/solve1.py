S = list(input())

ACGT = ["A","T","C","G"]

start,end = 0,0
best = 0
# while start <= len(S): 
#     if S[start] in ACGT:
#         if S[end] in ACGT:
#             best = max(best,end - start + 1)
#             end += 1
#         else:
#             start = end + 1
#             end += 1
#     else:
#         start += 1
#         end += 1

for i in range(len(S)):
    for j in range(i,len(S)):
         if S[j] not in ACGT:
              break
         best = max(best,j-i+1)
        

print(best)

    
    

