class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        x = 0
        y = 0

        while x < len(s) and y < len(t):

            if s[x]==t[y]:
                y +=1
            x +=1

        return len(t) - y       
        