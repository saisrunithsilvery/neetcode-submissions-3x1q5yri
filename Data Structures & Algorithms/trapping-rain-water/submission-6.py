from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        trapped = 0
        result = 0
        while l < r :

            if  leftMax <= rightMax:
                x =(min(leftMax, rightMax)- height[l] )
                result +=x

                leftMax = max(leftMax, height[l])
                l +=1


            else:
                x =(min(leftMax, rightMax)- height[l] )
                result +=x
                rightMax = max(rightMax, height[r])
                r -=1
        return result

