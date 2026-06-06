class Solution:
    def validPalindrome(self, s: str) -> bool:

        k = 0 
        i = 0
        j = len(s)-1
        while k < 2 and i < j:
            if s[i]!=s[j]:
                k +=1 

                if s[j-1]==s[i]:
                    j -=1

                if s[i+1]==s[j]:
                    i +=1

            else: 
                i +=1
                j -=1
           

                
             
         
        return k < 2        