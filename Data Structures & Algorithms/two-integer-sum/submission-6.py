class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x ={}

        for i, j in enumerate(nums):

            rem = target - j
            if rem in x:
                return [x[rem], i]

            x[j]=i    