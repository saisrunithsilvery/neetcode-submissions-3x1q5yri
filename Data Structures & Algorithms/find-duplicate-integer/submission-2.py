class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        slow = nums[0]
        fast = nums[nums[0]]

        while True:

            if slow == fast:
                break

            slow = nums[slow]
            fast = nums[nums[fast]]

        second = slow
        first = 0
        while True:

            if first == second:
                break

            first = nums[first]
            second = nums[second]    





        return first        



