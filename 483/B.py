N,Q = map(int,input().split())
K = list(map(int,input().split()))

cards = [i for i in range(1,N+1)]

left,right = [],[]
for k in K:
    left,right = cards[:k],cards[k:]
    left = [x * -1 for x in left] 
    left.reverse()
    cards = left + right

for i in cards:
    print(i)
    

