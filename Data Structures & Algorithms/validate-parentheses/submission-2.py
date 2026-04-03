class Solution:
    def isValid(self, s: str) -> bool:
        stack={ ')':'(', ']':'[', '}':'{' }
        x=[]
        for i in s:
            if x and i in stack :
                a=x.pop()
                if a!= stack[i]:
                    return False
            else:        
                x.append(i)
        return True if len(x) == 0 else False


        