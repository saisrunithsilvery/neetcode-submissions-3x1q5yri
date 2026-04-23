class Solution:
    def isHappy(self, n: int) -> bool:
        
        set1 = set()

        def solv(n):
            x = 0
            if n == 1:
                return True
            if n in set1 :
                return False    

            for digit in str(n):
                digit = int(digit)
                
                x +=digit**2
            set1.add(n)
            return solv(x)    

        return solv(n)    

