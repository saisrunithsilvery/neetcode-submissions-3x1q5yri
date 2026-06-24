class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # stores indices, heights kept increasing
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
        # Use height 0 at the very end to flush everything out
            cur_height = heights[i] if i < n else 0
            # While the bar on top of the stack is taller than current,
            # it can't extend further right — so finalize its rectangle
            while stack and heights[stack[-1]] > cur_height:
                index = stack.pop()
                height = heights[index]
                # Left boundary is the new top of stack (after popping)
                left = stack[-1] if stack else -1
                width = i - left -1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
        