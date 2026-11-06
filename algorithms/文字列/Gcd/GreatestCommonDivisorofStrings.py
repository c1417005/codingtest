class Solution:
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        s = str1
        t = str2
        result = []
        gcd = math.gcd(len(s),len(t))
        times = len(s)//gcd
        result = s[:gcd]
       
        for i in range(times):
            if t[:gcd] != s[i * gcd : (i+1)*gcd]:
                return ""
           
  
        return result
        
            