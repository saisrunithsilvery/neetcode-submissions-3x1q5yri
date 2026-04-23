class Solution:
    def myPow(self, x: float, n: int) -> float:

        

        res = 0

        def res(n):

            if n == 0: return 1

            if n ==1:
                return x

            elif n%2 == 1:
                y = res((n-1)//2)
                return x*y*y
            else:
                y = res(n//2)
                return y*y 

        a = res(abs(n))

        if n < 0:
            return 1/a
        else :
            return a     
        