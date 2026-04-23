class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                tmp                     = matrix[top][l+i]
                matrix[top][l+i]        = matrix[r-i][l]   # left → top
                matrix[bottom-i][l]     = matrix[r][r-i]   # bottom → left
                matrix[bottom][r-i]     = matrix[l+i][r]      # right → bottom
                matrix[top+i][r]        = tmp                   # top → right

            l += 1
            r -= 1
            

            