class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result =[0]*(len(temperatures))
        stack =[]
        for i in range(0,len(temperatures),):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                x = stack.pop()
                result[x] = i - x

            stack.append(i)

        return result