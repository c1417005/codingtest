class Solution:
    def reverseWords(self, s: str) -> str:
        given_s = list(s.strip().split())
        
        
        # for i in range(len(given_s)):
        #     if (i == 0  or i == len(given_s)-1) and given_s[i] == " ":
        #         dup_s.remove(" ")
        #     print("dup_s:",dup_s)

        times = len(given_s)//2
        left,right = 0,len(given_s)-1

        for _ in range(times):
            given_s[left],given_s[right] = given_s[right],given_s[left]
            left += 1
            right -= 1

        return " ".join(given_s)

S = Solution()
print(S.reverseWords(" a b c "))