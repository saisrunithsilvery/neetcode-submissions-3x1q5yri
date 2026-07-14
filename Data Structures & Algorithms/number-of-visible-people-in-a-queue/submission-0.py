class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        stack = []
        result = [0]*(len(heights))

        for index in range(len(heights)-1, -1,-1):
            count = 0

            while stack and heights[stack[-1]] < heights[index]:
                stack.pop()
                count +=1

            if stack :
                count +=1

            result[index] = count        
            stack.append(index)    

        return result    

        