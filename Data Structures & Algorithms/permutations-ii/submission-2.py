from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []

        count = Counter(nums)

        def solve():
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return

            for num in count:
                if count[num] == 0:
                    continue

                permutation.append(num)
                count[num] -= 1

                solve()

                count[num] += 1
                permutation.pop()

        solve()
        return result