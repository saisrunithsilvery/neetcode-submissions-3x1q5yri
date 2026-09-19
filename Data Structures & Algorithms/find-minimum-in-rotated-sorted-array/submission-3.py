class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1      # min is strictly right of mid
            else:
                r = mid          # min is at mid or to its left

        return nums[l]           # l == r, pointing at the minimum