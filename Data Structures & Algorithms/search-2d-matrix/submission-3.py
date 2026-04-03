class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i  in matrix:
            if target >= i[0] and target<= i[-1]:
                l=0
                r= len(matrix[0])-1
                print(i)
                while l <= r:
                    mid = (l+r)//2
                    print(mid)
                    if i[mid] == target:
                        return True
                    elif i[mid]> target:
                        r =mid -1
                    else:
                        l =mid +1
                        print(r)
        return False                                