class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix :
            return False
        row = 0
        column_len =len(matrix[0])
        row_len=len(matrix)

        while row< len(matrix):

            if matrix[row][0] <= target <= matrix[row][column_len-1]:
                low=0
                high =  column_len-1
                
                while low <= high:
                    mid = (low+high)//2
                    if target==matrix[row][mid]:
                        return True
                    elif target>matrix[row][mid]:
                        low =mid+1
                    else:
                        high =mid-1    
                row +=1        
                            
            else:
                row +=1

        return False                 
        