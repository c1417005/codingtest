a = [10,-5,0,29,6,2,77,8]

def is_add(n:int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

def main():

    for i in a:
        is_add(i)
        if is_add(i):
            print(f"{i}は偶数です")
        else:
            print(f"{i}は奇数です")

main()