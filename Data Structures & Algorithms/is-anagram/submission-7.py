class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False
        s1 = {}
        t1 = {}

        for i in range(0, len(s)):
            s1[s[i]] = s1.get(s[i], 0)+1
           

        for i in range(len(s1)):

            s1[t[i]] = s1.get(t[i], 0)-1

            if s1[t[i]] < 0:
                return False

        return True        




        



        