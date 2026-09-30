from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate an n x n matrix 90 degrees clockwise, in place.
        Time: O(n^2)  |  Space: O(1)
        """
        n = len(matrix)

        # Step 1: Transpose (swap across the main diagonal)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
