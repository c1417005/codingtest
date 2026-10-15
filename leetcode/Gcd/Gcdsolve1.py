
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            if len1 % k or len2 % k: 
                return False
            # kで割って余りがある → False

            n1, n2 = len1 // k, len2 // k
            
            base = str1[:k]
            # baseは繰り返されている文字列。
            return str1 == n1 * base and str2 == n2 * base 
            # str1 もstr2もbaseの繰り返しであれば、true

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""