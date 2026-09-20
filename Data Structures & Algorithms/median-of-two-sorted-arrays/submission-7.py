class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        total = len(nums1) + len(nums2)


        left = 0
        right = len(nums1)

        while left <= right :

            i = (left +right)//2

            j = (total+1)//2 - i

            left_sub_end = nums1[i-1] if i > 0 else float('inf')*(-1)
            right_sub_start = nums1[i] if i < len(nums1) else float('inf')

            left_sub_end1 = nums2[j-1] if j > 0 else float('inf')*(-1)
            right_sub_start1 = nums2[j] if j < len(nums2) else float('inf')


            if left_sub_end <= right_sub_start1 and left_sub_end1 <= right_sub_start :

                if total% 2 == 1:
                    return max(left_sub_end, left_sub_end1)

                else:
                    return (min(right_sub_start1, right_sub_start) + max(left_sub_end, left_sub_end1))/2

            elif left_sub_end > right_sub_start1:
                right = i - 1

            else:
                left = i+1

        return float(1)            



