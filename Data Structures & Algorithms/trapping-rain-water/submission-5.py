class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        water = 0

        while left <= right:
            if leftMax <= rightMax:
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
                right -= 1

        return water