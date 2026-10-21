import sys

def main():
    input = sys.stdin.readline
    H,W = map(int,input().split())
    field = [input().strip() for _ in range(H)]

    dh = (0,1,0,-1)
    dw = (1,0,-1,0)

    for h in range(H):
        for w in range(W):
            if field[h][w] == 's':
                sh,sw = h,w
            elif field[h][w] == 'g':
                gh,gw = h,w

    seen = [[False] * W for _ in range(H)]
    seen[sh][sw] = True

    stack = [(sh,sw)]

    while stack:
        h,w = stack.pop()
        for i in range(4):
            nh,nw = h + dh[i], w + dw[i]
            #進んだ先の４方向をチェック。dが3までチェックし、もしifに引っ掛かるなら次のforに行けないので、外のwhileに戻る
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if field[nh][nw] == '#' or seen[nh][nw]:
                continue

            stack.append((nh,nw))
            seen[nh][nw] = True

    print("Yes" if seen[gh][gw] else "No")
        

main()


