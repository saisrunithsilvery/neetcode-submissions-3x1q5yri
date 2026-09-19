class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        result = 0


        for index in range(0, len(heights)):

            while stack and heights[stack[-1]] > heights[index]:
                
                last_index = stack.pop()
                if stack:
                    width = index - stack[-1] - 1
                else:
                    width = index

                area = width*heights[last_index]

                result = max(area, result)
                

            stack.append(index)

        n = len(heights)
        while stack:

            last_index = stack.pop()

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            area = width * heights[last_index]
            result = max(result, area)        


        return result        

        