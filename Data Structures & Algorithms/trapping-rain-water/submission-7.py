from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        trapped = 0
        result = 0
        while l <=r :

            if  leftMax <= rightMax:
                leftMax = max(leftMax, height[l])
                x =(leftMax- height[l] )
               
                result +=x
                l +=1


            else:
                rightMax = max(rightMax, height[r])
                x =(rightMax- height[r] )
                result +=x
                r -=1
        return result

