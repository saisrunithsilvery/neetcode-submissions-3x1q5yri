class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans ={}
        if not s or not t :
            return False

        if len(s)!=len(t):
            return False   
        for i in s:
            ans[i]=ans.get(i, 0)+1

        for j in t:
            if j not in ans:
                return False

            ans[j]= ans[j]-1 
            if ans[j] <0:
                return False

        return True               
