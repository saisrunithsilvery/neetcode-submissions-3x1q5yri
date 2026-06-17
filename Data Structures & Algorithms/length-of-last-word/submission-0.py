class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        for i in range(len(s)-1, -1, -1):

            if s[i]!= " ":
                j = i
                while s[j]!= " ":
                    j -=1
                return i-j          

                  

        