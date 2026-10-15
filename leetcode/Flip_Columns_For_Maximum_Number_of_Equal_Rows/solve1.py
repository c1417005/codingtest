class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        matrix = matrix
        new_mx = []
        matrix_size = len(matrix)
        results = 1

        for i in range(matrix_size):
            m = matrix[i]
            # print("m :",m)
            if m[0] == 1:
                for i in range(len(m)):
                    m[i] = m[i] ^ 1
            new_mx.append(m)
        print("newm :",new_mx)
        


        for i in range(len(new_mx)-1):
            mi = new_mx[i]
            for j in range(len(new_mx)-1):
                if i == j+1:
                    continue
                if  mi == new_mx[j+1]:
                    results += 1
                

                print("mi:",mi,"new_mi",new_mx[i+1],"results",results)

        return results
            
s = Solution()
print(s.maxEqualRowsAfterFlips([[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,1,1,0,1,1,1,0,1,1,1]]))

# results = 1 の初期値に根拠がない。空一致でも1になる
# ペア単位で数えているので、3行一致するグループは本来3だがペアは6個検出される
# range(len(new_mx)-1) — 外側は最後の行を、内側は j+1 なので最初の行を候補から落としている
# 内側の反転ループが外側と同じ i を使い回している(今回はたまたま動くが危険)
# m = matrix[i] は参照なので matrix を破壊的に書き換えている

        




