class Solution:
    def tribonacci(self, n: int) -> int:

        n1 = 0
        n2 = 1 
        n3 = 1

        if n == 0:
            return n1
        elif n == 1:
            return n2
        elif n == 2:
            return n3

        for i in range(3, n+1):

            temp = n1+n2+n3   
            n1 = n2
            n2 = n3
            n3 = temp

        return temp    


            

