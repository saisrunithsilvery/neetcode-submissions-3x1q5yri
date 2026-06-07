class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        l = 0
        r = len(arr)-1
        x = -1
        while r > -1:

            temp = arr[r]
            arr[r]= x
            x = max(temp, x)
            r -=1
        return arr    
            
                  



        