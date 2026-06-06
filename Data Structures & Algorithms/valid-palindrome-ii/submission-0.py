class Solution:
    def validPalindrome(self, s: str) -> bool:

        k = 0 
        i = 0
        j = len(s)-1
        while k < 2 and i < j:
            if s[i]!=s[j]:
                k +=1   
                
             
            i +=1
            j -=1
            
        return k < 2        