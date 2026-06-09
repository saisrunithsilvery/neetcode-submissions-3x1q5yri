from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack will store indices of bars in increasing height order
        stack = [-1]  # sentinel to handle width when rectangle goes to the start
        best = 0

        # Add sentinel bar of height 0 to flush remaining bars in stack at the end
        heights.append(0)

        for i, h in enumerate(heights):
            # If current bar is smaller, it ends rectangles for taller bars
            while stack[-1] != -1 and heights[stack[-1]] > h:
                mid = stack.pop()
                height = heights[mid]

                left_smaller = stack[-1]   # index of previous smaller element
                right_smaller = i          # current index is next smaller element

                width = right_smaller - left_smaller - 1
                best = max(best, height * width)

            stack.append(i)

        heights.pop()  # optional: restore input
        return best
        [7,1,7,2,2,4]