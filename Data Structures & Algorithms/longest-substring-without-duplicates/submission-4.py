class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        r = 0
        visited = set()
        length = 0
        for r in range(0, len(s)):

            while s[r] in visited:
                visited.remove(s[l])
                l +=1
            visited.add(s[r])    

            length = max(length, r - l+1)
        return length        

        