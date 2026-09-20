class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        total = m +n

        left = 0
        right = m

        while left <= right:

            # partition in nums1
            i = (left + right) // 2

            # partition in nums2
            j = (total + 1) // 2 - i

            
            left_sub_end = nums1[i - 1] if i > 0 else float('-inf')
            right_sub_start = nums1[i] if i < m else float('inf')

            left_sub_end1 = nums2[j - 1] if j > 0 else float('-inf')
            right_sub_start1 = nums2[j] if j < n else float('inf')

            if left_sub_end1 <= right_sub_start and left_sub_end <= right_sub_start1:

                if (m + n) % 2 == 1:
                    return float(max(left_sub_end, left_sub_end1))

                # Even number of elements
                return (
                    max(left_sub_end, left_sub_end1) +
                    min(right_sub_start1, right_sub_start)
                ) / 2

            # nums1 partition is too far right
            elif left_sub_end > right_sub_start1:
                right_sub_start = i - 1

            # nums1 partition is too far left
            else:
                left_sub_end = i + 1