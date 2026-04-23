class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                tmp                     = matrix[top][l+i]
                matrix[l][l+i]        = matrix[r-i][l]   # left → top
                matrix[r-i][l]     = matrix[r][r-i]   # bottom → left
                matrix[r][r-i]     = matrix[l+i][r]      # right → bottom
                matrix[l+i][r]        = tmp                   # top → right

            l += 1
            r -= 1
            

            