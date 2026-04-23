class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x = 0
        result =0
        for i, c in enumerate(num2):
            sum1 =""
            carry = 0
            for ch in reversed(num1):
                a = int(ch)*int(c)+carry
                if a >=10:
                    carry = a // 10  # ✅
                    
                else :
                    carry = 0
                sum1 = str(a%10)+sum1      
            if carry >0:
                result +=int(str(carry)+sum1)*(10**(len(num2) - 1 - i) ) # ✅ instead of 10**i))
            else:

                result +=(int(sum1)*(10**(len(num2) - 1 - i)))  # ✅ instead of 10**i))    
        return str(result)            







            



        