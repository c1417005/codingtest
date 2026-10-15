


class Solution:


    
    def mergeAlternately(self,word1: str, word2: str) -> str:
        result_word = ""
        nw1 = 0
        nw2 = 0
        for _ in range(max(len(word1),len(word2))):
            if nw1 < len(word1):
                result_word += word1[nw1]
                nw1 += 1

            if nw2 < len(word2):
                result_word += word2[nw2]
                nw2 += 1

        return result_word









