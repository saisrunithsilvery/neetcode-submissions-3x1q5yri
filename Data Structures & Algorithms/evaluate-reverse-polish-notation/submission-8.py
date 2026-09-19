class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = {'+', '-', '*', '/'}
        for val in tokens:
            if val in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                z = 0

                if val == '+':
                    z = a+b

                elif val ==  '*':
                    z = a*b 
                elif val == '/':
                    if b == 0:
                        z = 0
                    else:
                        z = int(a/b )
                else :
                    z = a-b

                stack.append(z)
            else:
                stack.append(val)

        return int(stack[-1]   )             





        