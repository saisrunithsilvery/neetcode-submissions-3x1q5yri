class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result =[]
        stack =[]
        for i in range(len(temperatures)-1, -1,-1):

            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()


            if stack:
                result.append(stack[-1]-i)
               

            else:
                result.append(0)    

            stack.append(i)
         
        result.reverse()

        return result