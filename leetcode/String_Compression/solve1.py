class Solution:
    def compress(self, chars: list[str]) -> list[str]:

        i = j = 0
        while(i<len(chars)-1):
            count = 0
            while (j<len(chars)-1):
                if chars[i] == chars[j]:
                    count += 1
                    j+=1
                else:
                    break
            if count == 1:
                
            i = j

                
            



        

    
                

        

                