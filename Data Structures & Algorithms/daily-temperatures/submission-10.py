class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)  # ← Initialize with zeros
        stack = []
        
        for i in range(len(temperatures)):
            # Pop all elements smaller than current temperature
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx  # ← Fill by index, not append
            
            stack.append(i)
        
        return result