import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        result = []
        for i in nums:
            x = bisect.bisect_left(result, i)

            if x == len(result):
                result.append(i)
            else:
                result[x] = i
        return len(result)            

        