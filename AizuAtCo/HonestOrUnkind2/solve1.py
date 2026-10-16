

N = int(input())

testimony_by_people = []
for _ in range(N):
    a = int(input())
    testimony = []
    for _ in range(a):
        testimony.append(tuple(map(int,input().split())))
    testimony_by_people.append(testimony)
#[[(1,0),(2,0)],[(1,1)...]]

best = 0
for i in range(1<<N):
    cnt = 0
    for j in range(len(testimony_by_people)):
        for k in testimony_by_people[j]:
            if ((i >> j) & 1): 
                if k[1] == 1:
                    cnt += 1
            else:
                if k[1] == 0:
                    cnt += 1
        best = max(cnt,best)

print(best)



