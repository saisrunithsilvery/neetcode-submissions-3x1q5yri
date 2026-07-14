class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        result = []
        stack = []
        for i in range(len(arr)):

            while stack and abs(x- arr[stack[-1]]) <= abs(x- arr[i]):

                if len(result) < k:
                    x = stack.pop()
                    result.append(arr[x])
                    
                else:
                    break

            stack.append(i)

        while len(result) < k and stack:
            result.append(arr[stack.pop()])    

        result.sort()
        return result                      



            

        