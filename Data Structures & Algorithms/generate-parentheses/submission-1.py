class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
    
        def backtrack(open, close, current):
            # Base: all 2n positions filled
            if len(current) == 2 * n:
                result.append("".join(current))
                return
            
            # Place '(' if we haven't used all n
            if open < n:
                current.append('(')
                backtrack(open + 1, close, current)
                current.pop()
            
            # Place ')' only if it keeps string valid
            if close < open:
                current.append(')')
                backtrack(open, close + 1, current)
                current.pop()
        
        backtrack(0, 0, [])
        return result
            