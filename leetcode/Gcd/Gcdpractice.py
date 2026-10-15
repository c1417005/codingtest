class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        n1, n2 = len(str1), len(str2)

        def isdivisol(k: int):
            if n1 % k or n2 % k:
                return False

        for i in range(min(n1, n2), 0, -1):
            isdivisol(i)
            base = str1[:(i)]
            # スライスは”その長さぶん”とる処理。インデックスではない
            if str1 == base * (n1 // i) and str2 == base * (n2 // i):
                return base

        return ""


s = Solution()
print("実行結果 : ", s.gcdOfStrings("abcabc", "abc"))
