class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights)-1
        longest =0
        while i<j:
            longest =max(longest, min(heights[i],heights[j])*(j-i))
            if heights[i]<=heights[j]:
                i=i+1
            else: j -=1
        return longest     





