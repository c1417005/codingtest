n = int(input())
a = list(map(int, input().split()))
k = int(input())
a_h = list(map(int, input().split()))

def selection_sort(h):
    num_of_move = 0
    for i in range(h,n):
        x = a[i]
        j = i-h
        while (j >= 0) and (x < a[j]):
            a[j+h] = a[j]
            j -= h
            num_of_move += 1
        a[j+h] = x
    print(num_of_move)

for h in a_h:
    selection_sort(h)