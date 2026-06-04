class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        
        lo, hi = min(strs), max(strs)
        for i, char in enumerate(lo):
            if hi[i] != char:
                return lo[:i]
        return lo     
        