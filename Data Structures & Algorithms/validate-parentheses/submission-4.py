class Solution:
    def isValid(self, s: str) -> bool:

        
        brakts = {
            ')': '(',
            '}' : '{',
            ']' :'[' 
        }
        stack = []

        
        for char in s :

            if char in brakts:
                if stack :
                    b = stack.pop()
                    if b != brakts[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)  

        if not stack :

            return True 
        else :
            return False          



        