class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        result = [0]*len(temperatures)

        stack = []


        for index in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[index]:
                x = stack.pop()
                days = index - x 
                result[x] = days
            stack.append(index)

        return result        
        