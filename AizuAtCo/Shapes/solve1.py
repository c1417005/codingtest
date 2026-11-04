N = int(input())

# S = []
# for i in range(N):
#     si = input()
#     S.append(si)

S = [input() for _ in range(N)]
T = [input() for _ in range(N)]


def rot(G):
    return ["".join(row) for row in zip(*G[::-1])]
# G[::-1] リスト逆順
# [ab, -> [cd,
#  cd]     ab]

# zip 各要素のx文字ずつ取り出す
# 
# zip([cd,  -> [ca,
#      ab])     db]
# 組み合わせると時計回りに反転

#回転の角度は、2本の折り返しの線がなす角の2倍になります。
# 今回の線は、横の中心線（上下反転の軸）と左上から右下への対角線（転置の軸）で、45度の角をなしています。
# そのため 45° × 2 = 90° の回転になります。

def norm(G):
    cells = [(i,j) for i in range(N) for j in range(N) if G[i][j] == "#"]# #の座標を得る
    bi,bj = min(cells) #[0]の値から順に比較。一番上、一番左の基準点を見つける。
    return {(i - bi,j - bj) for i,j in cells} # 見つけた基準点が原点にくるように平行移動

target = norm(T)
for _ in range(4):
    if norm(S) == target:
        print("Yes")
        break
    S = rot(S)
else:
    print("No")

#右に90度回転。 公式(i,j) -> (j,N-1-i)

# 形が一致するか判定する 座標変換
# 回転後のグリッドを出力する	zip