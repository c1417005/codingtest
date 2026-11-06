class Solution:
    def reverseVowels(self, s: str) -> str:
        given_s = s
        length_s = len(given_s)
        vowels = set("aiueoAIUEO")
        vowel_stack = []
        dup_s = list(given_s) #strに対してスライスなのでstr
        


        for i in range(length_s):
            if given_s[i] in vowels:#set に対するinはO(1)
                dup_s[i] = "*"#replaceは非破壊的変更。戻り値を受け取る必要あり。
                vowel_stack .append(given_s[i])#appendは破壊的変更
        

        for j in range(length_s):
            if dup_s[j] == "*":
                last_v = vowel_stack.pop()
                dup_s[j] = last_v

            
        return "".join(dup_s)#(区切り文字).join(リスト等)
                

