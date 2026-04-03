class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a={}
        b={}
        for i in s:
            if i not in a:
                a[i] =1
            else:
                a[i] +=1
        for i in t:
            if i not in b:
                b[i] =1
            else:
                b[i] +=1
        for i in set(s):
            if a[i]!= b.get(i, 0):
                return False 
        return True                            

        