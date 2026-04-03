from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []  # indices, temps strictly increasing from top to bottom when scanning right->left

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                res.append(stack[-1] - i)
            else:
                res.append(0)

            stack.append(i)

        res.reverse()
        return res