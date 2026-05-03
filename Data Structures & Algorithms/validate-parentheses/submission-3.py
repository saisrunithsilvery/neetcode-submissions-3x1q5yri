class Solution:
    def isValid(self, s: str) -> bool:
        stack={ ')':'(', ']':'[', '}':'{' }
        x=[]
        for i in s:
            if  i in stack :
                a=x.pop() if x != [ ] else  False
                if a!= stack[i]:
                    return False
            else:        
                x.append(i)
        return True if len(x) == 0 else False


        