import sys

def main():
    input = sys.stdin.readline
    H,W = map(int,input().split())
    field = [input().strip() for _ in range(H)]

    
    dh = (1,0,-1,0)# 上下方向の移動
    dw = (0,1,0,-1)# 左右方向の移動

    for h in range(H):
        for w in range(W):
            if field[h][w] == 's':# スタートを探す
                sh,sw = h,w
            elif field[h][w] == 'g':# ゴールを探す
                gh,gw = h,w


    seen = [[False] * W for _ in range(H)] # 探索履歴の配列
    seen[sh][sw] = True #スタートをTrueに
    stack = [(sh,sw)]  # これから調べる予定のマスの記録
    while stack:
        h,w = stack.pop()
        for d in range(4):
            nh,nw = h + dh[d],w + dw[d]
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if field[nh][nw] == '#' or seen[nh][nw]:
                continue
            seen[nh][nw] = True
            stack.append((nh,nw))

    print("Yes" if seen[gh][gw] else "No")

main()