class Solution:
    def maxArea(self, heights: List[int]) -> int:


        result = 0
        l = 0 
        r = len(heights)-1 

        while l < r:

            volume = min(heights[l], heights[r])*(r-l)

            result = max(volume, result)

            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1

        return result            

        