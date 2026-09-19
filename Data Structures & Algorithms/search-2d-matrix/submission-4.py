class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        # Step 1: Find the correct row
        top = 0
        bottom = m - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        else:
            return False

        # Step 2: Binary search inside that row
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False