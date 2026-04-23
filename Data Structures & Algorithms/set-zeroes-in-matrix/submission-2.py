class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix[0])
        n = len(matrix)

        row0 = any(matrix[0][j] == 0 for j in range(m))  # did row 0 originally have a zero?
        col0 = any(matrix[i][0] == 0 for i in range(n))  # did col 0 originally have a zero?

        for i in range(1, n):
            for j in range(0, m):
                
                if matrix[i][j] ==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):

            if matrix[i][0] ==0:
                for j in range(0, m):
                    matrix[i][j] = 0
        for j in range(1, m):

            if matrix[0][j] ==0:
                for i in range(0, n):
                    matrix[i][j] = 0

        if row0 :
            for j in range(0, m):
                matrix[0][j] = 0

        if col0 :
            for i in range(0, n):
                matrix[i][0] =0                    

      
                                    