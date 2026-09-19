class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        r = 0
        visit = set()
        result = 0

        while r < len(s):

            while s[r]  in visit :
                visit.remove(s[l])
                l +=1

            result = max(result, r-l +1)
            visit.add(s[r])
            r +=1
            

        return result        



        