class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aiueoAIUEO")
        chars = list(s)
        left, right = 0, len(chars) - 1
        #left,rightは両端

        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1

            #両端からスタートし、子音だったら次へ
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            #両方母音が見つかったら、交換。次へ。

        return "".join(chars)