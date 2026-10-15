n = int(input())
S = list(input())

stack = []


def bracket(S):
    for s in S:
        if s == "(":
            stack.append(s)

        else:
            if len(stack) == 0:
                print("No")
                return

            stack.pop()

    if len(stack) == 0:
        print("Yes")
    else:
        print("No")


bracket(S)
