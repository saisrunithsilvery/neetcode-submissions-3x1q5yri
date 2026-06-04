class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        x1 = strs[0]
        x2 = strs[1]

        len1 = min(len(x1), len(x2))
        i = 0
        while i < len1:
            if x1[i]!= x2[i]:
                break
            i +=1    

        if i == 0:
            return ""
        else:
            return str(x1[:i])        