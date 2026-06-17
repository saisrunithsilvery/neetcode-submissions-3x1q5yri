class Solution:
    def minOperations(self, s: str) -> int:

        point1 = "0"
        point2 = "1"
        min1 = 0
        min2 = 0

        for i in range(len(s)):

            if s[i]!=point1:
                min1 +=1
            if s[i] != point2:
                min2 +=1
            point1, point2 = point2, point1
        return min(min1, min2)            


        