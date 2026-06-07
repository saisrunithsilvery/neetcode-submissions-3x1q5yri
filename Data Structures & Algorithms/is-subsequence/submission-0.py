class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x =0
        y =0

        while x < len(s) and y < len(t):

            if s[x]==t[y]:
                x +=1
            y +=1
       
        return x == len(s)       
        